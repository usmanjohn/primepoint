"""Portfolio views — copied from the bank version (portfel/view.py).

DEMO changes, nothing else touched:
  * no Oracle: portfel_get / portfel_process / portfel_vs_balans are not here, and
    portfel_home shows a message instead of going to the database;
  * the data are the synthetic svod files written by make_fake_svod.py.
"""
import io
import os
import datetime

import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pathlib import Path

from . import forms
from .functions import prepare_df, generate_risk_chart, find_summa_and_npl, generate_pie_chart
from functions import common_functions

BASE_DIR = Path(__file__).resolve().parent.parent

portfel_input_folder = BASE_DIR / "datasets" / "portfel" / "input"
portfel_svod_folder = BASE_DIR / "datasets" / "portfel" / "svod"
portfel_all_folder = BASE_DIR / "datasets" / "portfel" / "all"
balans_svod_folder = BASE_DIR / "datasets" / "balans" / "svod"


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
            else:
                # DEMO: no Oracle here — only the synthetic months exist.
                messages.warning(request, "В демо-версии данные есть только на 1-е число последних 12 месяцев.")
    else:
        form = forms.DateInputForm()
    return render(request, 'portfel/home.html', {'form':form})

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
