"""
Two views: the page (form + portfolio) and the same portfolio as an Excel file.

The form uses GET, so a portfolio has its own link: /client_portfolio/?contragentid=123&pdate=2026-10-01
— send it to a colleague and they see the same thing.
"""
from datetime import date

import oracledb
from django.http import HttpResponse
from django.shortcuts import render

from . import excel as excel_file
from . import logic, queries


def _params(request):
    """(contragentid, pdate, error). Error is a Russian message or None."""
    cid = request.GET.get("contragentid", "").strip()
    pd = request.GET.get("pdate", "").strip()
    if not cid.isdigit():
        return None, None, "Введите ID контрагента (только цифры)."
    try:
        pdate = date.fromisoformat(pd)
    except ValueError:
        return None, None, "Выберите дату."
    return int(cid), pdate, None


def _portfolio(request):
    """(portfolio, error): load from Oracle and build."""
    cid, pdate, error = _params(request)
    if error:
        return None, error
    try:
        data = queries.load_client(cid, pdate)
    except oracledb.Error as e:
        return None, f"Ошибка базы данных: {e}"
    if not data["accounts"] and not data["deals"]:
        return None, f"На {pdate:%d.%m.%Y} у контрагента {cid} нет счетов с остатком и живых сделок."
    return logic.build(data, cid, pdate), None


def page(request):
    ctx = {"form": {"contragentid": request.GET.get("contragentid", ""),
                    "pdate": request.GET.get("pdate", "")}}
    if "contragentid" in request.GET:
        ctx["p"], ctx["error"] = _portfolio(request)
    return render(request, "client_portfolio/page.html", ctx)


def excel(request):
    p, error = _portfolio(request)
    if error:
        return HttpResponse(error, status=400, content_type="text/plain; charset=utf-8")
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = (
        f'attachment; filename="portfolio_{p["contragentid"]}_{p["pdate"]:%Y%m%d}.xlsx"')
    excel_file.write(p, response)
    return response
