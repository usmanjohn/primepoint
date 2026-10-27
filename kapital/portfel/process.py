import pandas as pd
import numpy as np
from functions import common_functions

def process_portfel_best(df, utils_path):
    utils_path_str = str(utils_path)
    
    # ==========================================
    # 1. LOAD UTILS & REFERENCE DATA
    # ==========================================
    try:
        loan_type_df = pd.read_excel(utils_path_str, sheet_name='loantype')
        client_type_df = pd.read_excel(utils_path_str, sheet_name='clients')
        minibank_df = pd.read_excel(utils_path_str, sheet_name='minibanks')
        anketa_ipoteka = pd.read_excel(utils_path_str, sheet_name='ipoteka_vtorichka')
        print('Utils read successfully!')
    except Exception as e:
        print(f'Problem reading utils! {e}')
        raise e

    anketa_ipoteka['passporter'] = anketa_ipoteka['passporter'].str.lower()
    df.columns = df.columns.str.lower()
    df = df.rename(columns={'branch': 'siteid', 'kvazi_x': 'kvazi'})

    # ==========================================
    # 2. INITIAL PREPROCESSING & CLEANING
    # ==========================================
    amount_cols = [
        'given_amount', 'brutto_95_amount', 'brutto_amount', '95413_amount', 
        '91501_amount', 'reserve_main_amount', 'reserve_int_amount', 
        'reserve_comission_amount', 'court_main_amount', 'court_int_amount', 
        '16405_amount', 'overdue_main_amount', 'int_amount', '16377_amount', 
        '16377_2_amount', 'peresmotren_amount', 'discount_amount'
    ]
    existing_amount_cols = [col for col in amount_cols if col in df.columns]
    df[existing_amount_cols] = df[existing_amount_cols].fillna(0)
    
    df['critical_amounts'] = df[existing_amount_cols].sum(axis=1)
    df['has_any_amount'] = np.where(df['critical_amounts'] > 0, 'yes', 'no')
    
    df['short_schet'] = df['schet'].astype(str).str[:3]
    df['is_corporate'] = np.where(df['short_schet'].isin(['125', '149']), 'no', 'yes')
    
    df['dealdate'] = pd.to_datetime(df['dealdate'], errors='coerce').dt.to_period("M") 
    
    # Standardize string formatting
    loan_type_df['loan_name'] = loan_type_df['loan_name'].astype(str).str.lower()
    loan_type_df['loan_type'] = loan_type_df['loan_type'].astype(str).str.lower()
    client_type_df['passport_fix'] = client_type_df['passport_fix'].astype(str).str.lower()
    df['rk_passport'] = df['rk_passport'].astype(str).str.lower()
    df['mk_passport'] = df['mk_passport'].astype(str).str.lower()
    df['pinfl'] = df['pinfl'].astype(str)
    
    # Overdue days bucketing
    df['overdue_days_max'] = df['overdue_days_max'].fillna(0)
    bins = [-np.inf, 30, 90, 180, 384, np.inf]
    labels = ['0-30', '30-90', '90-180', '181-364', '365+']
    df['overdue_days'] = pd.cut(df['overdue_days_max'], bins=bins, labels=labels)
    df['category'] = pd.to_numeric(df['category'], errors='coerce').fillna(1)
    df['department'] = df['department'].fillna('No') 
    df['currency'] = df['currencyid'].apply(lambda x: 'local' if x == 0 else 'global')

    # ==========================================
    # 3. MERGES
    # ==========================================
    df = df.merge(minibank_df[['minicode', 'branch']], left_on='toboid', right_on='minicode', how='left')
    df = df.merge(loan_type_df, left_on='rk_passport', right_on='loan_name', how='left')
    df = df.merge(client_type_df, on='dealid', how='left')
    
    mask_client = df['dealid'].isin(client_type_df['dealid'])
    df.loc[mask_client, 'loan_type'] = df.loc[mask_client, 'passport_fix']

    # ==========================================
    # 4. NPL LOGIC
    # ==========================================
    # 4.1 Base NPL Calculation
    days_map = {"0-30": 1, "30-90": 2, "90-180": 3, "181-364": 4, "365+": 5}
    cond_1 = df["overdue_days"].map(days_map).fillna(1).astype(int)
    cond_2 = df["category"]
    cond_3 = np.where(
        (df["court_main_amount"] > 0) | (df["court_int_amount"] > 0), 3, 1
    )
    cond_4 = np.where((df["95413_amount"] > 0) | (df["91501_amount"] > 0), 5, 1)

    # --- NEW: Step 1. Track the source condition before using np.maximum ---
    conditions = [cond_1, cond_2, cond_3, cond_4]
    labels = ["overdue_days", "category", "court_amount", "95413_91501_amount"]

    # Find which condition index drove the maximum value
    max_idx = np.argmax(conditions, axis=0)
    base_npl = np.maximum.reduce(conditions)

    # Map index to text description
    df["description"] = [labels[idx] for idx in max_idx]

    # --- Handle everything_is_zero override ---
    everything_is_zero = (
        (df["brutto_amount"] == 0)
        & (df["court_main_amount"] == 0)
        & (df["95413_amount"] == 0)
        & (df["91501_amount"] == 0)
    )
    df["npl_category"] = np.where(everything_is_zero, 1, base_npl)
    df.loc[everything_is_zero, "description"] = "everything_is_zero"

    # Keep a backup of the individual row's base NPL category for comparison later
    df["base_npl_category"] = df["npl_category"]


    # --- 4.2 Group Updates (Contragent & PINFL) ---
    valid_mask = (df["critical_amounts"] != 0) & (df["npl_category"].notna())

    # Contragent ID max spread
    contragent_mask = valid_mask & df["contragentid"].notna()
    df.loc[contragent_mask, "npl_category"] = df.groupby("contragentid")[
        "npl_category"
    ].transform("max")

    # PINFL max spread
    real_pinfl_mask = df["pinfl"].notna() & (
        ~df["pinfl"].isin(["0", "00000000000000"])
    )
    final_pinfl_mask = valid_mask & real_pinfl_mask
    df.loc[final_pinfl_mask, "npl_category"] = df[real_pinfl_mask].groupby(
        "pinfl")["npl_category"].transform("max")


    # --- NEW: Step 2. Append Escalation Info if the category changed ---
    escalated_mask = df["npl_category"] > df["base_npl_category"]

    # Use a custom function or np.where to tag how it escalated
    df.loc[escalated_mask, "description"] = (
        "Contragent/PINFL"
    )

    # Clean up temporary tracking column if desired
    df.drop(columns=["base_npl_category"], inplace=True)

    print("NPL Value Counts:\n", df["npl_category"].value_counts())

    # ==========================================
    # 5. DEPARTMENT & PASSPORT LOGIC
    # ==========================================
    df['department'] = np.where(
        (df['department'] == "No") | (df['schet'].astype(str) == '11101'),
        '01-Кредитный департамент',
        df['department']
    )
    
    df['department'] = np.where(
        (df['is_corporate'] == 'no') & (df['department'] == '01-Кредитный департамент'),
        '02-Розничный департамент', 
        df['department']
    )

    # Map Passports based on department rules
    conditions = [
        (df['department'] == '03-Малое кредитование'),
        (df['department'] == '04-Андерайтинговая служба'),
        (df['schet'].astype(str) == '11101'),
        (df['department'] == '01-Кредитный департамент'),    
        (df['department'] == '02-Розничный департамент')
    ]
    choices = [
        df['mk_passport'],
        'андерайтинговая служба',
        'факторинг',
        'корпоратив кредит',
        df['loan_type'],
    ]
    df['passport'] = np.select(conditions, choices, default=df['loan_type'])
    
    # Cleanup strings & Map short acronyms
    df['passport'] = df['passport'].str.replace("микрокредит ип в наличной форме", 'кредит ип в наличной форме')
    df['department'] = df['department'].str.replace("01-Розничный департамент", '02-Розничный департамент')
    df['department'] = df['department'].astype(str).str.replace("04-Андерайтинговая служба", '01-Кредитный департамент')
    
    # Ipoteka passport override
    df = df.merge(anketa_ipoteka, left_on='dealid', right_on='anketa', how='left')
    ipoteka_mask = df['dealid'].isin(anketa_ipoteka['anketa'])
    df.loc[ipoteka_mask, 'passport'] = df.loc[ipoteka_mask, 'passporter'] 

    # Fix MK passports where empty
    indices = (df['department'] == '03-Малое кредитование') & (df['passport'].isin([np.nan, 'nan']))
    df.loc[indices, 'passport'] = df.loc[indices, 'mk_passport']

    # Final department acronym mapping
    dept_map = {
        '01-Кредитный департамент': 'kk',
        '02-Розничный департамент': 'rk',
        '03-Малое кредитование': 'mk', 
        '06-Цифровое розн.кредитование': 'sk'
    }
    df['department'] = df['department'].replace(dept_map)

    # ==========================================
    # 6. OKED & FINAL CALCULATIONS
    # ==========================================
    df['rnk_id'] = df['rnk_id'].fillna(0).astype(int)
    try:
        df['int_rate_amount'] = (df['int_rate'] * df['brutto_95_amount']) / 100
        df['oked_corp_num'] = pd.to_numeric(df['oked_corp'], errors='coerce').fillna(0)
        df['oked_personal_num'] = pd.to_numeric(df['oked_personal'], errors='coerce').fillna(0)
        oked_conds = [
            df['oked_corp_num'] > 0,
            df['oked_personal_num'] > 0,
            df['passport'] == "онлайн микрозаем"
        ]
        oked_choices = [df['oked_corp_num'], df['oked_personal_num'], 64100]
        df['oked'] = np.select(oked_conds, oked_choices, default=96000)
        df['oked'] = df['oked'].astype(int).astype(str).str.zfill(5)
    except:
        pass
    # ==========================================
    # 7. FILTERING & TYPE ENFORCEMENT
    # ==========================================
    columns_to_keep = [
        'arcdate', 'contragentid', 'dealid', 'rnk_id', 'contragentname', 'branch', 'toboid', 
        'schet', 'department', 'passport', 'rk_passport', 'mk_passport', 'oked_personal', 
        'oked_corp', 'oked', 'kvazi', 'currencyid', 'currency', 'category', 'overdue_days_max', 
        'valuedate', 'given_amount', 'brutto_95_amount', 'brutto_amount', '95413_amount', 
         '91501_amount', 'reserve_main_amount', 
        'reserve_int_amount', 'reserve_comission_amount', 'court_main_amount', 
        'court_int_amount', '16405_amount', 'overdue_main_amount', 'int_amount', 
        '16377_amount', '16377_2_amount', 'peresmotren_amount', 'discount_amount','int_rate', 'pinfl', 'is_corporate', 
        'critical_amounts', 'overdue_days', 'npl_category', 'has_any_amount', 'int_rate_amount', 'description'
    ]
    existing_cols = [col for col in columns_to_keep if col in df.columns]
    df = df[existing_cols].copy()

    # Enforce Strings
    string_cols = ['branch', 'department', 'passport', 'rk_passport', 'mk_passport', 
                   'kvazi', 'pinfl', 'currency', 'oked', 'oked_personal', 'oked_corp']
    for col in string_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().replace(['nan', 'None', '<NA>'], np.nan).fillna('other')

    # Enforce Numerics (Vectorized)
    numeric_cols = [
        'given_amount', 'brutto_95_amount', 'brutto_amount', '95413_amount', '91501_amount', 'reserve_main_amount', 'reserve_int_amount', 
        'reserve_comission_amount', 'court_main_amount', 'court_int_amount', '16405_amount', 
        'overdue_main_amount', 'int_amount', '16377_amount', '16377_2_amount','peresmotren_amount', 
        'discount_amount',  'int_rate', 
        'int_rate_amount', 'critical_amounts', 'overdue_days_max', 'category', 'npl_category',
        'contragentid', 'dealid', 'rnk_id', 'toboid', 'schet'
    ]
    valid_num_cols = [col for col in numeric_cols if col in df.columns]
    df[valid_num_cols] = df[valid_num_cols].apply(pd.to_numeric, errors='coerce').fillna(0)

    # Missing indicators log
    print('__________________________Attention!____________________________')
    print("Passports missing:\n", df[(df['passport'] == 'other') & (df['brutto_95_amount'] > 0)][['department','dealid',"rk_passport", 'mk_passport']])
    print("Minibank missing:\n", df[(df['toboid'] == 0) & (df['brutto_95_amount'] > 0)][['department','brutto_amount','dealid','branch']])
    
    # Dates
    df['given_date'] = pd.to_datetime(df['valuedate'], errors='coerce').dt.strftime('%Y-%m')
    
    # ==========================================
    # 8. AGGREGATION & FINAL RETURN
    # ==========================================
    df_svod = df[df['critical_amounts'] > 0].copy()
    df_svod['deal_count'] = 1
    
    groupby_keys = [
        'given_date', 'branch', 'toboid', 'department', 'passport', 'currency', 
        'oked', 'category', 'npl_category', 'overdue_days', 'is_corporate', 'has_any_amount'
    ]
    columns_to_sum = amount_cols + ['int_rate_amount', 'deal_count']

    existing_keys = [k for k in groupby_keys if k in df_svod.columns]
    existing_sums = [c for c in columns_to_sum if c in df_svod.columns]

    ready_df = df_svod.groupby(existing_keys, dropna=False)[existing_sums].sum().reset_index()
    df = df.drop(['given_date', 'has_any_amount', 'overdue_days', 'is_corporate', 'currency'], axis=1, errors='ignore')
    print(f"Final Ready Portfel Brutto Amount => {ready_df['brutto_amount'].sum():,.2f}") 
    return ready_df, df