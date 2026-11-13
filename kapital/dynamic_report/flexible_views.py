import io
from pathlib import Path

import pandas as pd
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent.parent
dynamic_summary_folder = BASE_DIR / "datasets" / "dynamics" / "summary"
filename = 'summary.parquet'

GROUPING_COLUMNS = [
    'report_date', 'filial', 'tobo', 'department',
    'passport', 'avto', 'kategoriya_origin', 'kategoriya_npl_90',
    'kategoriya_straxovka', 'sud'
]

SUM_COLUMNS = [
    'vidacha_tekushiy_summa', 'brutto_95_summa', 'brutto_summa',
    'protsent_16309_summa', 'protsent_16377_summa', 'protsent_16379_summa',
    'spisat_95413_summa', 'spisat_91501_summa', 'reserve_summa',
    'pogashen_tekushiy_summa', 'straxovka_summa', 'straxovka_brutto_95_summa',
    'npl_summa'
]

# Russian names shown on the page and in the Excel header. The code stays visible under each
# name on the page, so if a name is not quite right, fix it here — nothing else changes.
COLUMN_LABELS = {
    'report_date': 'Отчётная дата',
    'filial': 'Филиал',
    'tobo': 'ТОБО (офис)',
    'department': 'Департамент',
    'passport': 'Паспорт продукта',
    'avto': 'Авто (первичка / вторичка)',
    'kategoriya_origin': 'Категория качества (исходная)',
    'kategoriya_npl_90': 'Категория качества (NPL 90+)',
    'kategoriya_straxovka': 'Категория (с учётом страховки)',
    'sud': 'Судебный статус',
    'vidacha_tekushiy_summa': 'Выдача за месяц',
    'brutto_95_summa': 'Портфель брутто + списанное (95413)',
    'brutto_summa': 'Портфель брутто (на балансе)',
    'protsent_16309_summa': 'Проценты, счёт 16309',
    'protsent_16377_summa': 'Проценты, счёт 16377',
    'protsent_16379_summa': 'Проценты, счёт 16379',
    'spisat_95413_summa': 'Списано, счёт 95413',
    'spisat_91501_summa': 'Списано, счёт 91501',
    'reserve_summa': 'Резерв',
    'pogashen_tekushiy_summa': 'Погашено за месяц',
    'straxovka_summa': 'Страховое возмещение',
    'straxovka_brutto_95_summa': 'Брутто с учётом страховки',
    'npl_summa': 'NPL',
}

MAX_ROWS_ON_PAGE = 2000   # more than this freezes the browser; the Excel file always has every row

_cache = {}               # the parquet is read once per file change, not on every click


def _load_summary():
    path = dynamic_summary_folder / filename
    mtime = path.stat().st_mtime
    if _cache.get('mtime') != mtime:
        df = pd.read_parquet(path)
        df['report_date'] = pd.to_datetime(df['report_date'])
        _cache.update(mtime=mtime, df=df)
    return _cache['df']


def _label(col):
    return COLUMN_LABELS.get(col, col)


@login_required
def dynamic_report(request):
    # 1. Load the data (from memory if the file has not changed)
    df = _load_summary()

    # 2. Options for the selectors
    filter_options = {
        'filials': sorted(df['filial'].dropna().unique()),
        'departments': sorted(df['department'].dropna().unique()),
        'passports': sorted(df['passport'].dropna().unique()),
        'min_date': df['report_date'].min().strftime('%Y-%m-%d') if not df.empty else '',
        'max_date': df['report_date'].max().strftime('%Y-%m-%d') if not df.empty else '',
    }
    grouping_available = [c for c in GROUPING_COLUMNS if c in df.columns]
    metrics_available = [c for c in SUM_COLUMNS if c in df.columns]

    # 3. URL inputs — anything not in the lists is ignored instead of crashing the page
    start_date = request.GET.get('start_date') or ''
    end_date = request.GET.get('end_date') or ''
    selected_filial = request.GET.get('filial') or 'All'
    selected_dept = request.GET.get('department') or 'All'
    selected_passport = request.GET.get('passport') or 'All'

    selected_metrics = [m for m in request.GET.getlist('metrics') if m in metrics_available] \
        or metrics_available
    selected_groupings = [g for g in request.GET.getlist('groupings') if g in grouping_available] \
        or [g for g in ['report_date', 'department'] if g in grouping_available]

    # 4. Filter
    filtered_df = df
    start_ts = pd.to_datetime(start_date, errors='coerce') if start_date else None
    end_ts = pd.to_datetime(end_date, errors='coerce') if end_date else None
    if start_ts is not None and not pd.isna(start_ts):
        filtered_df = filtered_df[filtered_df['report_date'] >= start_ts]
    if end_ts is not None and not pd.isna(end_ts):
        filtered_df = filtered_df[filtered_df['report_date'] <= end_ts]
    if selected_filial != 'All':
        filtered_df = filtered_df[filtered_df['filial'] == selected_filial]
    if selected_dept != 'All':
        filtered_df = filtered_df[filtered_df['department'] == selected_dept]
    if selected_passport != 'All':
        filtered_df = filtered_df[filtered_df['passport'] == selected_passport]

    # 5. Group and sum. dropna=False: rows with an empty filial/category are kept as their own
    #    line ("—") instead of silently vanishing from the totals.
    if not filtered_df.empty:
        final_df = (filtered_df.groupby(selected_groupings, dropna=False)[selected_metrics]
                    .sum().reset_index())
        if 'report_date' in final_df.columns:
            final_df['report_date'] = final_df['report_date'].dt.strftime('%Y-%m-%d')
    else:
        final_df = pd.DataFrame(columns=selected_groupings + selected_metrics)

    # 6. Excel — Russian column names, frozen header, amounts as numbers with separators
    if request.GET.get('download') == 'excel':
        out = final_df.rename(columns=_label)
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            out.to_excel(writer, index=False, sheet_name='Отчёт')
            ws = writer.sheets['Отчёт']
            ws.freeze_panes = 'A2'
            for i, col in enumerate(final_df.columns, start=1):
                letter = ws.cell(row=1, column=i).column_letter
                ws.column_dimensions[letter].width = max(14, len(_label(col)) + 2)
                if col in selected_metrics:
                    for cell in ws[letter][1:]:
                        cell.number_format = '#,##0.00'
        buffer.seek(0)
        name = f"financial_report_{start_date or filter_options['min_date']}_{end_date or filter_options['max_date']}.xlsx"
        response = HttpResponse(
            buffer.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename="{name}"'
        return response

    # 7. Page: rows as ready-made cells, so the template does not search every row for every column
    columns = selected_groupings + selected_metrics
    metric_set = set(selected_metrics)
    headers = [{'code': c, 'label': _label(c), 'is_num': c in metric_set} for c in columns]

    total_rows = len(final_df)
    shown = final_df.head(MAX_ROWS_ON_PAGE)
    rows = []
    for values in shown[columns].itertuples(index=False):
        row = []
        for col, v in zip(columns, values):
            empty = v is None or (not isinstance(v, str) and pd.isna(v))
            is_num = col in metric_set
            row.append({'v': None if empty else v, 'is_num': is_num,
                        'neg': is_num and not empty and v < 0})
        rows.append(row)

    totals = []
    if total_rows:
        sums = final_df[selected_metrics].sum()
        totals = [{'v': sums[c], 'neg': sums[c] < 0} for c in selected_metrics]

    context = {
        'filter_options': filter_options,
        'grouping_options': [{'code': c, 'label': _label(c)} for c in grouping_available],
        'metric_options': [{'code': c, 'label': _label(c)} for c in metrics_available],
        'selected_metrics': selected_metrics,
        'selected_groupings': selected_groupings,
        'start_date': start_date,
        'end_date': end_date,
        'selected_filial': selected_filial,
        'selected_dept': selected_dept,
        'selected_passport': selected_passport,
        'headers': headers,
        'rows': rows,
        'totals': totals,
        'group_count': len(selected_groupings),
        'total_rows': total_rows,
        'rows_cut': total_rows > MAX_ROWS_ON_PAGE,
        'max_rows': MAX_ROWS_ON_PAGE,
    }
    return render(request, 'dynamic_report/flexible_report.html', context)
