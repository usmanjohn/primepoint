"""
The pages of fast search. Two pages only:

    /fast-search/                    every report (every .sql file in fast_search/sql/)
    /fast-search/client_deals/       one report: its form, and after «Показать» the result

The form sends GET, so a result has its own address: send it to a colleague and they get
the same result. «Excel» is the same address with &excel=1.
"""
from datetime import date

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
    context = {"report": rep, "fields": fields, "show_sql": request.user.is_staff}
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
        if table.size <= reports.CSV_MAX_CELLS:
            return download(table, name)
        context["errors"] = [f"{len(table):,} строк — слишком много для Excel. Сузьте параметры.".replace(",", " ")]

    query = request.GET.copy()
    query.pop("excel", None)
    context.update(reports.preview(table))
    context.update({"ran": True, "seconds": f"{seconds:.1f}", "query": query.urlencode()})
    return render(request, "fast_search/report.html", context)


def download(table, name):
    """The whole result as .xlsx (or .csv when it is too big to write as Excel in time)."""
    stamp = date.today().isoformat()
    if table.size > reports.EXCEL_MAX_CELLS:
        response = HttpResponse(reports.to_csv(table), content_type="text/csv; charset=utf-8")
        response["Content-Disposition"] = f'attachment; filename="{name}_{stamp}.csv"'
        return response
    response = HttpResponse(reports.to_xlsx(table, name),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f'attachment; filename="{name}_{stamp}.xlsx"'
    return response
