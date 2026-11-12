# -*- coding: utf-8 -*-
"""
Three pages:
  balans_home   - choose a date. If that date is already saved, go straight to the result.
  balans_get    - load the balance for the date from Oracle and save it as a parquet file.
  balans_result - read the parquet file and show the report (all maths: functions.build_report).
"""
import datetime
import os
from pathlib import Path

import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from functions import common_functions

from . import forms, queries
from .functions import build_report

BASE_DIR = Path(__file__).resolve().parent.parent
balans_svod_folder = BASE_DIR / "datasets" / "balans" / "svod"


def file_for(date_str):
    return balans_svod_folder / f"balans_{date_str}.parquet"


@login_required
def balans_home(request):
    form = forms.DateInputForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        date_str = str(form.cleaned_data['selected_date'])
        request.session[f"balans_date_str_{request.user.id}"] = date_str
        request.session[f"balans_filepath_svod_{request.user.id}"] = str(file_for(date_str))
        if file_for(date_str).exists():
            messages.success(request, "Данные за эту дату уже загружены.")
            return redirect('balans-result')
        return redirect('balans-get')
    return render(request, 'balans/home.html', {'form': form})


@login_required
def balans_get(request):
    date_str = request.session.get(f"balans_date_str_{request.user.id}")
    try:
        selected_date = datetime.date.fromisoformat(date_str)
    except (TypeError, ValueError):
        messages.warning(request, "Сначала выберите дату.")
        return redirect('balans-home')

    os.makedirs(balans_svod_folder, exist_ok=True)
    conn = None
    try:
        conn = common_functions.get_oracle_connection()
        cursor = conn.cursor()
        cursor.execute(queries.balans_script, {'pdate': selected_date})
        rows = cursor.fetchall()
        if not rows:
            messages.warning(request, 'Данных за эту дату ещё нет.')
            return redirect('balans-home')
        df = pd.DataFrame(rows, columns=['arcdate', 'account', 'currency', 'amount'])

        # Profit of the current year is still sitting in classes 4 and 5 (they close only at
        # year end), so it is added to 31206 «Sof foyda (zarar)» - otherwise the balance does
        # not add up. Added ONCE: 31206 can have a row per currency, and adding it to each
        # row would count the profit twice.
        acc = df['account'].astype(str)
        profit = abs(df.loc[acc.str.startswith('4'), 'amount'].sum()) - abs(df.loc[acc.str.startswith('5'), 'amount'].sum())
        is_31206 = acc.str[:5] == '31206'
        if is_31206.any():
            df.loc[is_31206.idxmax(), 'amount'] += profit
        else:
            print('WARNING: no 31206 row - the profit of the year is not in the equity')

        tmp = file_for(date_str).with_suffix('.tmp')
        df.to_parquet(tmp, index=False)
        tmp.replace(file_for(date_str))          # never leaves a half-written file behind
    except Exception as e:
        import traceback
        traceback.print_exc()
        messages.error(request, f"Ошибка при загрузке из базы: {e}")
        return redirect('balans-home')
    finally:
        if conn:
            conn.close()

    messages.success(request, f"Баланс за {selected_date:%d.%m.%Y} загружен.")
    return redirect('balans-result')


@login_required
def balans_result(request):
    date_str = request.session.get(f"balans_date_str_{request.user.id}")
    if not date_str or not file_for(date_str).exists():
        date_str = str(common_functions.find_recent_date(file_name='balans'))
    if not file_for(date_str).exists():
        messages.warning(request, "Нет данных. Сначала выберите дату.")
        return redirect('balans-home')

    df = pd.read_parquet(file_for(date_str))
    df.columns = ['arcdate', 'account', 'currency', 'amount']
    return render(request, 'balans/result.html', build_report(df, date_str))
