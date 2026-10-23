"""
The pages of the collateral app. Every view is short: it reads the address, asks
process.py for the numbers and gives them to a template.

NO DATE TO CHOOSE
The queries always return the state right now. «Обновить из базы» runs them and saves
the result under today's date; the page opens the newest saved file. Older files stay
as chips at the top, so you can still look back (?date=2026-10-20).

HOW THE DRILL-DOWN WORKS (no JavaScript)
Every choice is a word in the address:

    /collateral/                                         everything, newest file
    /collateral/?date=2026-10-22&kind=car                only cars
    /collateral/?date=2026-10-22&kind=car&brand=Chevrolet
    /collateral/?date=2026-10-22&kind=car&brand=Chevrolet&made_year=2019

A click on a row of a card adds one more word; a click on a breadcrumb removes the words
after it. So every view of the data has its own link: send it to a colleague and they
see the same thing.
"""
from datetime import date
from urllib.parse import urlencode

from django.contrib import messages
from django.http import FileResponse, Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from . import process, queries

# Who may delete saved days: False = anyone who can open the page,
# True = only users with «staff status» in the Django admin.
ONLY_STAFF_DELETES = False


def chosen_day(request):
    """?date=2026-10-20 if that file exists, otherwise the newest file (None if there is none)."""
    try:
        day = date.fromisoformat(request.GET.get("date", ""))
        if process.file_for(day).exists():
            return day
    except ValueError:
        pass
    return process.latest_day()


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
    """The part of the link after '?': date=2026-10-22&kind=car&brand=Chevrolet"""
    return urlencode([("date", day.isoformat())] + list(filters))


def breadcrumbs(day, filters):
    """«Всё обеспечение › Автотранспорт › Chevrolet»: each crumb links to the filters up to it."""
    crumbs = [{"title": "", "label": "Всё обеспечение", "link": address(day, [])}]
    for n, (column, value) in enumerate(filters, start=1):
        title, label = process.filter_label(column, value)
        crumbs.append({"title": title, "label": label, "link": address(day, filters[:n])})
    return crumbs


def home(request, error=None):
    """The main page: the newest saved file (or the clicked one) with the chosen filters."""
    day = chosen_day(request)
    saved = process.saved_days()
    context = {"saved": saved, "error": error, "today": date.today(),
               "saved_total": f"{sum(s['bytes'] for s in saved) / 1e6:.1f} МБ"}
    if day is None:                      # nothing downloaded yet: only the «Обновить» button
        return render(request, "collateral/page.html", context)

    filters = read_filters(request)
    context.update(process.build_page(process.read_day(day), day, filters, page_number(request)))
    context.update({
        "day": day,
        "updated": process.updated_at(day),
        "filters": filters,
        "link": address(day, filters),          # the current view, to add one more filter
        "crumbs": breadcrumbs(day, filters),
    })
    return render(request, "collateral/page.html", context)


@require_POST
def refresh(request):
    """«Обновить из базы»: run the three queries now, save as today's file, show it."""
    try:
        process.save_today()
    except Exception as error:          # no database, wrong table name, no pyarrow ...
        return home(request, error=f"Не удалось загрузить данные из базы: {error}")
    return redirect("collateral")


def deal(request, dealid):
    """Every filled field of one collateral deal."""
    day = chosen_day(request)
    if day is None:
        raise Http404("Данные ещё не загружены")
    card = process.deal_card(process.read_day(day), dealid, process.accounts_of(day))
    if card is None:
        raise Http404("Такой сделки обеспечения нет в этом файле")
    return render(request, "collateral/deal.html", {
        "day": day, "card": card, "back": address(day, read_filters(request))})


@require_POST
def delete(request):
    """
    «Удалить выбранные»: remove the ticked days (all their files). The newest day is kept,
    and nothing happens unless «Да, удалить» is ticked too — a plain form, no JavaScript.
    """
    if ONLY_STAFF_DELETES and not request.user.is_staff:
        return HttpResponseForbidden("Удалять файлы может только сотрудник с правами staff")
    if not request.POST.get("confirm"):
        messages.warning(request, "Ничего не удалено: отметьте «Да, удалить».")
        return redirect("collateral")
    removed = []
    for text in request.POST.getlist("day"):
        try:
            day = date.fromisoformat(text)
        except ValueError:
            continue
        if process.delete_day(day):
            removed.append(day.strftime("%d.%m.%Y"))
    if removed:
        messages.success(request, "Удалено: " + ", ".join(removed))
    else:
        messages.warning(request, "Ничего не удалено (последний день удалить нельзя).")
    return redirect("collateral")


def accounts(request):
    """Collateral against the 945xx off-balance accounts."""
    day = chosen_day(request)
    context = {"day": day, "saved": process.saved_days()}
    if day is None:
        return render(request, "collateral/accounts.html", context)
    table, accounts_table = process.read_day(day), process.accounts_of(day)
    if accounts_table is None:
        error = process.accounts_error_file(day)
        context["error"] = error.read_text(encoding="utf-8") if error.exists() else None
    else:
        context.update(process.accounts_page(table, accounts_table))
    return render(request, "collateral/accounts.html", context)


def accounts_excel(request):
    """The 945xx accounts with a balance and no collateral deal, as .xlsx."""
    day = chosen_day(request)
    if day is None or process.accounts_of(day) is None:
        raise Http404("Счета 945xx за этот день не загружены")
    table = process.orphans_excel(process.accounts_of(day))
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f'attachment; filename="accounts_945_{day.isoformat()}.xlsx"'
    table.to_excel(response, index=False, sheet_name="Счета без залога")
    return response


def excel(request):
    """The rows of the current view as an .xlsx file (all of them, not one page)."""
    day = chosen_day(request)
    if day is None:
        raise Http404("Данные ещё не загружены")
    table = process.excel_table(process.read_day(day), read_filters(request))
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f'attachment; filename="collateral_{day.isoformat()}.xlsx"'
    table.to_excel(response, index=False, sheet_name="Обеспечение")
    return response


def parquet_file(request):
    """The saved parquet file, as a download."""
    day = chosen_day(request)
    if day is None:
        raise Http404("Данные ещё не загружены")
    path = process.file_for(day)
    return FileResponse(open(path, "rb"), as_attachment=True, filename=path.name)


def params(request):
    """
    Help page: every parameter that exists in the database (live query, only when the
    button is pressed), which of them the app already uses, and the finished SQL to copy.
    """
    used = {}
    for kind, params_of_kind in [("Авто", queries.CARS), ("Недвижимость", queries.PROPERTY),
                                 ("Прочее", queries.others_flat()), ("Общие", queries.COMMON)]:
        for name, (column, label) in params_of_kind.items():
            used[name] = f"{kind}: {column}"
    context = {"sql": [("Авто", queries.SQL_CARS),
                       ("Недвижимость", queries.SQL_PROPERTY),
                       ("Прочее", queries.SQL_OTHERS),
                       ("Счета 945xx", queries.SQL_ACCOUNTS),
                       ("Счета 945xx без залога (FIND_ORPHANS)", queries.SQL_ORPHANS),
                       ("Все параметры", queries.SQL_PARAM_NAMES)]}
    if "run" in request.GET:
        try:
            names = queries.load_param_names()
            context["names"] = [{"name": r.paramname, "deals": process.number(r.deals),
                                 "example": r.example, "used": used.get(r.paramname)}
                                for r in names.itertuples()]
        except Exception as error:
            context["error"] = f"Не удалось выполнить запрос: {error}"
    return render(request, "collateral/params.html", context)
