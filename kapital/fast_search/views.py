"""
The pages of fast search. Two pages only:

    /fast-search/                    every report (every .sql file in fast_search/sql/)
    /fast-search/client_deals/       one report: its form, and after «Показать» the result

The form sends GET, so a result has its own address: send it to a colleague and they get
the same result. «Excel» is the same address with &excel=1.
"""
from datetime import date
from io import BytesIO

from django.http import Http404, HttpResponse
from django.shortcuts import render

from . import reports


def index(request):
    """Every report, as cards."""
    return render(request, "fast_search/index.html", {"reports": reports.all_reports()})


def report(request, name):
    """One report: the form; with ?run the result; with ?excel the result as a file."""
    rep = reports.read_report(name)
    if rep is None:
        raise Http404("Нет такого отчёта")

    fields = [dict(f, value=request.GET.get(f["name"], "")) for f in rep["fields"]]
    context = {"report": rep, "fields": fields}
    if "run" not in request.GET and "excel" not in request.GET:
        return render(request, "fast_search/report.html", context)

    values, errors = reports.read_values(rep, request.GET)
    if errors:
        context["errors"] = errors
        return render(request, "fast_search/report.html", context)
    try:
        table, seconds = reports.get_table(rep, values)
    except Exception as error:                  # an Oracle error: show it on the page
        context["oracle_error"] = str(error)
        return render(request, "fast_search/report.html", context)

    if "excel" in request.GET:
        return download(table, name)

    query = request.GET.copy()
    query.pop("excel", None)
    context.update(reports.preview(table))
    context.update({"ran": True, "seconds": f"{seconds:.1f}", "query": query.urlencode()})
    return render(request, "fast_search/report.html", context)


def download(table, name):
    """The whole result as .xlsx (or .csv when it is too big for Excel)."""
    stamp = date.today().isoformat()
    if len(table) > reports.EXCEL_MAX_ROWS:
        response = HttpResponse(content_type="text/csv; charset=utf-8")
        response["Content-Disposition"] = f'attachment; filename="{name}_{stamp}.csv"'
        response.write("﻿")                # so Excel opens the Russian letters right
        table.to_csv(response, index=False, sep=";")
        return response
    buffer = BytesIO()
    table.to_excel(buffer, index=False, sheet_name=name[:31])
    response = HttpResponse(buffer.getvalue(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f'attachment; filename="{name}_{stamp}.xlsx"'
    return response
