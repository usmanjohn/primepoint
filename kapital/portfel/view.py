import polars as pl
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import io
import getpass,oracledb,os,json,datetime
import os
import datetime
from django.contrib.auth.decorators import login_required
from . import forms
from . import queries
from .functions import prepare_df, generate_risk_chart, find_summa_and_npl, generate_pie_chart, process_balans
from .process import process_portfel_best
from functions import common_functions

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from pathlib import Path
from django.urls import reverse
BASE_DIR = Path(__file__).resolve().parent.parent


portfel_input_folder = BASE_DIR / "datasets" / "portfel" / "input"
portfel_svod_folder = BASE_DIR / "datasets" / "portfel" / "svod"
portfel_all_folder = BASE_DIR / "datasets" / "portfel" / "all"
balans_svod_folder = BASE_DIR / "datasets" / "balans" / "svod"
utils_path = BASE_DIR / "utils" / "useforauto.xlsx"
@login_required
def portfel_home(request):
    if request.method == 'POST':
        form = forms.DateInputForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['selected_date']
            date_str = str(selected_date)
            request.session[f"portfel_date_str_{request.user.id}"] = date_str
            portfel_filepath_svod = f"{portfel_svod_folder}/svod_{date_str}.parquet"
            portfel_filepath_all = f"{portfel_all_folder}/all_{date_str}.parquet"
            portfel_filepath_raw = f"{portfel_input_folder}/raw_{date_str}.parquet"
            balans_filepath_svod = f"{balans_svod_folder}/svod_{date_str}.parquet"

            if os.path.exists(portfel_filepath_svod):
                request.session[f"portfel_filepath_svod_{request.user.id}"] = portfel_filepath_svod
                messages.success(request, "Data is already processec, you can see results!")
                next_view = request.session.pop(f"portfel_next_view_{request.user.id}", None)
                
                if next_view:
                    return redirect(next_view)
                else:
                    return redirect('portfel-result', dept_type = 'total')
            elif os.path.exists(portfel_filepath_raw):
                print('we have not svod file but we already have raw data, so going to process')
                request.session[f'portfel_filepath_raw_{request.user.id}'] = portfel_filepath_raw
                messages.success(request, "Raw Data exist, but not svod, starting ...")
                return redirect('portfel-process')
            else:
                print('We have neither svod nor raw data, so connecting to db...')
                messages.success(request, "We have neither svod nor raw data, so connecting to db...")
                return redirect('portfel-get')
    else:
        form = forms.DateInputForm()
    return render(request, 'portfel/home.html', {'form':form})
@login_required
def portfel_get(request):
    # Ensure directories exist
    os.makedirs(portfel_input_folder, exist_ok=True)
    os.makedirs(portfel_svod_folder, exist_ok=True)
    os.makedirs(portfel_all_folder, exist_ok=True)
    os.makedirs(balans_svod_folder, exist_ok=True)
    conn = None
    pq_writer = None
    file_written = False
    portfel_date_str = request.session.get(f"portfel_date_str_{request.user.id}")
    if portfel_date_str:
        try:
            selected_date = datetime.datetime.strptime(portfel_date_str, '%Y-%m-%d').date()
        except ValueError:
            messages.warning(request, "The Date selected is unfamiliar")
            return redirect('portfel-home')
    else:
        messages.warning(request, "No date found in session.")
        return redirect('portfel-home')
    portfel_filepath_raw = f"{portfel_input_folder}/raw_{selected_date}.parquet"
    request.session[f"portfel_filepath_raw_{request.user.id}"] = portfel_filepath_raw
    if os.path.exists(portfel_filepath_raw):
        messages.success(request, "The File already exists, so processing")
        return redirect('portfel-process')    
    try:
        conn = common_functions.get_oracle_connection()
        batch_generator = conn.fetch_df_batches(
            queries.best_portfel_script, 
            parameters={'pdate': selected_date},
            size=100000  # Stream in highly optimized 100k row chunks
        )
        for odf in batch_generator:
            arrow_table = pa.table(odf)
            if pq_writer is None and arrow_table.num_rows == 0:
                break  # Stops processing, file_written remains False
            if pq_writer is None:
                pq_writer = pq.ParquetWriter(portfel_filepath_raw, arrow_table.schema)
            pq_writer.write_table(arrow_table)
            file_written = True
    except Exception as e:
        import traceback
        traceback.print_exc()
        print('Error happened on Portfolio query:', e)
        messages.error(request, f"Database or extraction error occurred: {e}")
        return redirect('portfel-home')
    finally:
        if pq_writer:
            pq_writer.close()
            print("Parquet file writer finalized and closed.")
        if conn:
            conn.close()
            print("Oracle database connection safely closed.")
    if not file_written:
        messages.warning(request, 'The data could not be fetched since it is not available yet!')
        return redirect('portfel-home')
    return redirect('portfel-process')
@login_required
def portfel_process(request):
    portfel_filepath_raw = request.session.get(f"portfel_filepath_raw_{request.user.id}")
    try:
        df_raw = pd.read_parquet(portfel_filepath_raw)
        svod_df, all_df = process_portfel_best(df_raw, utils_path)
        portfel_date_str = request.session.get(f'portfel_date_str_{request.user.id}')
        portfel_filepath_svod = f"{portfel_svod_folder}/svod_{portfel_date_str}.parquet"
        portfel_filepath_all = f"{portfel_all_folder}/all_{portfel_date_str}.parquet"
        request.session[f"portfel_filepath_svod_{request.user.id}"] = portfel_filepath_svod
        if os.path.exists(portfel_filepath_svod):
            print('The file is already proceessed, skipping ...')
            messages.success(request, 'portfel is already svod')
            next_view = request.session.pop(f"portfel_next_view_{request.user.id}", None)
            if next_view:
                return redirect(next_view)
            else:
                return redirect('portfel-result', dept_type = 'total')
        else:
            print('filepath does not exist, creating ...')
            svod_df.to_parquet(portfel_filepath_svod)
            print("svod Svod file is saved")
            try:
                all_df.to_parquet(portfel_filepath_all)
                print("All File is saved")
            except Exception as e:
                print(f"All file is not saved: {e}")
            next_view = request.session.pop(f"portfel_next_view_{request.user.id}", None)
            if next_view:
                return redirect(next_view)
            else:
                return redirect('portfel-result', dept_type = 'total')
    except Exception as e:
        messages.error(request, f'{e} The database is not fetched since it is not yet available')
        return redirect('portfel-home')
    return render(request, 'portfel/process.html')

@login_required
def portfel_result(request, dept_type = 'total'):
    selected_date = request.session.get(f"portfel_date_str_{request.user.id}")
    portfel_filepath_svod = request.session.get(f'portfel_filepath_svod_{request.user.id}')
    if selected_date is None and portfel_filepath_svod is None:
        selected_date = common_functions.find_recent_date()
        portfel_date_str = str(selected_date)
        request.session[f"portfel_date_str_{request.user.id}"] = portfel_date_str
        portfel_filepath_svod = f"{portfel_svod_folder}/svod_{portfel_date_str}.parquet"
        request.session[f"portfel_filepath_svod_{request.user.id}"] = portfel_filepath_svod
    portfel_date_str = str(selected_date)
    if os.path.exists(portfel_filepath_svod):
        print(f'{portfel_filepath_svod} exists')
        try:
            df = pd.read_parquet(portfel_filepath_svod) 
            df = df.rename({'passport_final':'passport'}, axis = 1) 
            df['short_passport'] = df['passport'].replace(common_functions.passport_map)
            if df.empty:
                messages.warning(request, 'Df is empty')
                return redirect('portfel-home')
        except Exception as e:        
            print(f"Detailed error: {e}")  # Print the exact error message
            messages.warning(request, f"Cant read the df: {e}") 
            return redirect('portfel-home')
        context = {'portfel_date_str':portfel_date_str,
                    'dept_type':dept_type}
        if dept_type == 'total':
            dept_ru_name = 'Все'
            template_name = 'portfel/result_total.html'                    
            content_all = find_summa_and_npl(df)
            content_rk = find_summa_and_npl(df, 'department', 'rk')
            content_mk = find_summa_and_npl(df, 'department', 'mk')
            content_kk = find_summa_and_npl(df, 'department', 'kk')
            grouped_rk = prepare_df(df, 'branch', 'rk')
            grouped_mk = prepare_df(df, 'branch', 'mk')
            grouped_kk = prepare_df(df, 'branch', 'kk')
            
            try:
                chart_rk  = generate_risk_chart(grouped_rk, group_col = 'branch', custom_color = '#1e3655')
                chart_mk  = generate_risk_chart(grouped_mk, group_col = 'branch', custom_color = '#174d39' )
                chart_kk  = generate_risk_chart(grouped_kk, group_col = 'branch', custom_color = '#5E4D21')
                
            except Exception as e:
                print(f"Error happened: {e}")
                messages.warning(request, f"Error happened during generating charts: {e}")
                return redirect('portfel-home')
            total_context = {
                "chart_rk": chart_rk,
                "chart_mk": chart_mk,
                "chart_kk": chart_kk,
            }

            try:
                context.update(content_all)
                context.update(content_rk)
                context.update(content_kk)
                context.update(content_mk)
                context.update(total_context)
            except Exception as e:
                print(f"Could not update the context: {e}")
                pass
            
        elif dept_type in ['all', 'kk','rk','mk']:
            if dept_type == 'all':
                color_choice = '#000e0f'
                dept_ru_name = 'Все'
            elif dept_type == 'kk':
                color_choice = '#5E4D21'
                dept_ru_name = 'Корпоративный'
            elif dept_type == 'rk':
                color_choice = '#1e3655'
                dept_ru_name = 'Розничный'
            elif dept_type == 'mk':
                color_choice = '#174d39'
                dept_ru_name = 'Малый'
            
            dept_name = dept_type
            cond_name = 'department'

            template_name = 'portfel/result_dept.html'
            content_dept = find_summa_and_npl(df, cond_name, dept_name)
            grouped_branch = prepare_df(df, 'branch', dept_name)
            grouped_passport = prepare_df(df, 'short_passport', dept_name)
            try:
                chart_branch  = generate_risk_chart(grouped_branch, group_col = 'branch', custom_color = color_choice)
                chart_passport  = generate_risk_chart(grouped_passport, group_col = 'short_passport', custom_color = color_choice)
                npl_pie_chart  = generate_pie_chart(df, dept = dept_type, group_col = 'npl_category')
                
            except Exception as e:
                print(f"Error happened: {e}")
                messages.warning(request, f"Error happened during generating charts: {e}")
                return redirect('portfel-home')
            prefix = dept_type
            context_new = {
                "chart_branch": chart_branch,
                "chart_passport": chart_passport,
                "npl_pie_chart": npl_pie_chart,
                'department_title': dept_type.upper(),
                'dept_ru_name':dept_ru_name,
                
                # We normalize the keys here so result_dept.html knows exactly what to look for!
                'portfel': content_dept.get(f'{prefix}_portfel', 0),
                'npl': content_dept.get(f'{prefix}_npl', 0),
                'npl_percent': content_dept.get(f'{prefix}_npl_percent', 0),
                'local_portfel': content_dept.get(f'{prefix}_local_portfel', 0),
                'global_portfel': content_dept.get(f'{prefix}_global_portfel', 0),
                'local_npl': content_dept.get(f'{prefix}_local_npl', 0),
                'global_npl': content_dept.get(f'{prefix}_global_npl', 0),
                'local_avg_percent': content_dept.get(f'{prefix}_local_avg_percent', 0),
                'global_avg_percent': content_dept.get(f'{prefix}_global_avg_percent', 0),
                'local_npl_percent': content_dept.get(f'{prefix}_local_npl_percent', 0),
                'global_npl_percent': content_dept.get(f'{prefix}_global_npl_percent', 0),
                'city_portfel': content_dept.get(f'{prefix}_city_portfel', 0),
                'village_portfel': content_dept.get(f'{prefix}_village_portfel', 0),
                'city_npl': content_dept.get(f'{prefix}_city_npl', 0),
                'village_npl': content_dept.get(f'{prefix}_village_npl', 0),
                'city_npl_percent': content_dept.get(f'{prefix}_city_npl_percent', 0),
                'village_npl_percent': content_dept.get(f'{prefix}_village_npl_percent', 0)
            }

            try:
                context.update(context_new)
            except Exception as e:
                print(f"Could not update the context: {e}")
                pass
        
        else: 
            message.warning(request, 'Invalid Department selected')
            return redirect('portfel-home')

    else:
        messages.warning(request, 'Portfel is not ready, please select a date to start with')
        return redirect('portfel-home')
    return render(request, template_name, context)

def download_portfel_summary(request):
    selected_date = request.session.get(f"portfel_date_str_{request.user.id}")
    selected_date_str = str(selected_date)
    portfel_filepath_svod = request.session.get(f'portfel_filepath_svod_{request.user.id}')
    if os.path.exists(portfel_filepath_svod):
        df = pd.read_parquet(portfel_filepath_svod)  
        if df.empty:
            messages.warning(request, 'Df is empty')
            return redirect('portfel-home')
        buffer = io.BytesIO()
        print(df.columns)
        if len(df.columns)==23:
                df.columns = ['Дата выдачы',"Филиаль","Регион","Банк филиали МФО раками","Валюта","Отделение","Описание кредита","ОКЕД","Является ли НПЛ?","Дни просрочки","Код категории качества",
                "Пол",'Тип контрагента','Юр./Физ.',"Основной кредит на балансе (эквивалент брутто)",'brutto_without_95413',"Остаток по кредиту на балансе (нетто)","Сумма резерва (эквивалент)","Ср. Процент",
                "Количество",'Категория Процент',"Стандарт качества"]
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='svod')
        buffer.seek(0)
        response = HttpResponse(
            buffer,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename="Portfel_{selected_date_str}.xlsx"'
        return response


def portfel_vs_balans(request):
    # Use standard session keys unless user-isolated keys are strictly required by design
    portfel_date_str = request.session.get(f"portfel_date_str_{request.user.id}")
    
    if not portfel_date_str:
        messages.warning(request, "No date found in session.")
        return redirect("portfel-home")
    try:
        selected_date = datetime.datetime.strptime(
            portfel_date_str, "%Y-%m-%d"
        ).date()
    except ValueError:
        messages.warning(request, "The selected date format is invalid.")
        return redirect("portfel-home")

    portfel_filepath = f"{portfel_svod_folder}/svod_{selected_date}.parquet"
    balans_filepath = f"{balans_svod_folder}/balans_{selected_date}.parquet"

    # Check if files exist safely
    if not os.path.exists(portfel_filepath):
        request.session[f"portfel_next_view_{request.user.id}"] = 'portfel-vs-balans'
        messages.error(
            request, f"Portfel file for {selected_date} are missing from storage, please select which date you want to see"
        )
        return redirect("portfel-home")

    if not os.path.exists(balans_filepath):
        request.session[f"balans_next_view_{request.user.id}"] = 'portfel-vs-balans'
        messages.error(
            request, f"Balans file for {selected_date} are missing from storage, please select which date you want to see"
        )
        return redirect("balans-home")
        
    # Read data
    portfel = pd.read_parquet(portfel_filepath)
    balans = pd.read_parquet(balans_filepath)
    
    # Process balans using the np.select logic we built
    balans = process_balans(balans)

    # Calculate Portfolio sums (Use float() conversion to prevent serialization errors in Django)
    p_brutto = float(portfel["brutto_amount"].sum())
    p_spisat = float(portfel["95413_amount"].sum())
    p_reserve = float(portfel["reserve_main_amount"].sum())

    # Calculate Balans sums
    b_sums = balans.groupby("type")["amount"].sum()
    b_brutto = float(b_sums.get("brutto", 0))*-1
    b_reserve = float(b_sums.get("reserve", 0))
    b_spisat = float(b_sums.get("spisat", 0))*-1

    # Construct structured matrix for the template looping
    comparison_data = [
        {
            "metric": "Brutto Amount",
            "portfel": p_brutto,
            "balans": b_brutto,
            "diff": p_brutto - b_brutto,
        },
        {
            "metric": "Reserve Main Amount",
            "portfel": p_reserve,
            "balans": b_reserve,
            "diff": p_reserve - b_reserve,
        },
        {
            "metric": "Spisat (95413)",
            "portfel": p_spisat,
            "balans": b_spisat,
            "diff": p_spisat - b_spisat,
        },
    ]

    context = {
        
        "selected_date": selected_date,
        "comparison_data": comparison_data,
        "totals": {
            "portfel": p_brutto + p_reserve + p_spisat,
            "balans": b_brutto + b_reserve + b_spisat,
            "diff": (p_brutto + p_reserve + p_spisat)
            - (b_brutto + b_reserve + b_spisat),
        },
    }

    return render(request, "portfel/balans_vs_portfel.html", context)
    
        

    