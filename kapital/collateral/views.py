"""
The pages of the collateral app. Every view is short: it reads the address, asks
process.py for the numbers and gives them to a template.

HOW THE DRILL-DOWN WORKS (no JavaScript)
Every choice is a word in the address:

    /collateral/?date=2026-10-01                                  everything
    /collateral/?date=2026-10-01&kind=car                         only cars
    /collateral/?date=2026-10-01&kind=car&brand=Chevrolet         only Chevrolets
    /collateral/?date=2026-10-01&kind=car&brand=Chevrolet&made_year=2019

A click on a row of a card adds one more word; a click on a breadcrumb removes the words
after it. So every view of the data has its own link: send it to a colleague and they
see the same thing.
"""
from datetime import datetime
from urllib.parse import urlencode

from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import render

from . import process, queries
from .forms import DayForm


def read_filters(request):
    """The filters from the address, in the order they were chosen: [('kind', 'car'), ...]."""
    allowed = process.filter_keys()
    filters = []
    for key, value in request.GET.items():
        if key in allowed and value and key not in dict(filters):
            filters.append((key, value))
    return filters


def page_number(request):
    """?page=3 → 3; anything else → 1."""
    text = request.GET.get("page", "1")
    return int(text) if text.isdigit() else 1


def address(day, filters):
    """The part of the link after '?': date=2026-10-01&kind=car&brand=Chevrolet"""
    return urlencode([("date", day.isoformat())] + list(filters))


def breadcrumbs(day, filters):
    """«Всё обеспечение › Автотранспорт › Chevrolet»: each crumb links to the filters up to it."""
    crumbs = [{"title": "", "label": "Всё обеспечение", "link": address(day, [])}]
    for n, (column, value) in enumerate(filters, start=1):
        title, label = process.filter_label(column, value)
        crumbs.append({"title": title, "label": label, "link": address(day, filters[:n])})
    return crumbs


def home(request):
    """The main page: the date form, then the numbers for the date and the chosen filters."""
    form = DayForm(request.GET or None)
    context = {"form": form, "saved": process.saved_days()}
    if not form.is_valid():
        return render(request, "collateral/page.html", context)

    day = form.cleaned_data["date"]
    try:
        table = process.read_day(day, refresh=form.cleaned_data["refresh"])
    except Exception as error:          # no database, wrong table name, no pyarrow ...
        context["error"] = f"Не удалось загрузить данные на {day:%d.%m.%Y}: {error}"
        return render(request, "collateral/page.html", context)

    filters = read_filters(request)
    context.update(process.build_page(table, day, filters, page_number(request)))
    context.update({
        "day": day,
        "filters": filters,
        "link": address(day, filters),          # the current view, to add one more filter
        "crumbs": breadcrumbs(day, filters),
        "saved_at": datetime.fromtimestamp(process.file_for(day).stat().st_mtime),
    })
    return render(request, "collateral/page.html", context)


def deal(request, dealid):
    """Every filled field of one collateral deal."""
    form = DayForm(request.GET)
    if not form.is_valid():
        raise Http404("Нет даты")
    day = form.cleaned_data["date"]
    if not process.file_for(day).exists():
        raise Http404("На эту дату данные ещё не загружены")
    card = process.deal_card(process.read_day(day), dealid)
    if card is None:
        raise Http404("Такой сделки обеспечения нет на эту дату")
    filters = read_filters(request)
    return render(request, "collateral/deal.html", {
        "day": day, "card": card, "back": address(day, filters)})


def excel(request):
    """The rows of the current view as an .xlsx file (all of them, not one page)."""
    form = DayForm(request.GET)
    if not form.is_valid():
        raise Http404("Нет даты")
    day = form.cleaned_data["date"]
    table = process.excel_table(process.read_day(day), read_filters(request))
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f'attachment; filename="collateral_{day.isoformat()}.xlsx"'
    table.to_excel(response, index=False, sheet_name="Обеспечение")
    return response


def parquet_file(request):
    """The saved parquet file of a date, as a download."""
    form = DayForm(request.GET)
    if not form.is_valid() or not process.file_for(form.cleaned_data["date"]).exists():
        raise Http404("Файла на эту дату нет")
    path = process.file_for(form.cleaned_data["date"])
    return FileResponse(open(path, "rb"), as_attachment=True, filename=path.name)


def params(request):
    """
    Help page: every parameter that exists in the database on a date (live query),
    which of them the app already uses, and the finished SQL to copy into your SQL tool.
    """
    form = DayForm(request.GET or None)
    used = {}
    for kind, params_of_kind in [("Авто", queries.CARS), ("Недвижимость", queries.PROPERTY),
                                 ("Прочее", queries.others_flat()), ("Общие", queries.COMMON)]:
        for name, (column, label) in params_of_kind.items():
            used[name] = f"{kind}: {column}"
    context = {"form": form, "sql": [("Авто", queries.SQL_CARS),
                                     ("Недвижимость", queries.SQL_PROPERTY),
                                     ("Прочее", queries.SQL_OTHERS),
                                     ("Все параметры на дату", queries.SQL_PARAM_NAMES)]}
    if form.is_valid():
        try:
            names = queries.load_param_names(form.cleaned_data["date"])
            context["names"] = [{"name": r.paramname, "deals": process.number(r.deals),
                                 "example": r.example, "used": used.get(r.paramname)}
                                for r in names.itertuples()]
        except Exception as error:
            context["error"] = f"Не удалось выполнить запрос: {error}"
    return render(request, "collateral/params.html", context)
