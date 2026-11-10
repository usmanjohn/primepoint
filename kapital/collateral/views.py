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

SUMMARY ONLY (2026-11-10): active collateral, cards and KPIs. There is no list of deals,
no page of one deal and no parquet download: the анкета-level fields are not kept.
"""
from datetime import date
from functools import wraps
from urllib.parse import urlencode

from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from . import process, queries

# THE SWITCH. False = the app is turned off: every page shows «временно отключено» and
# nothing is read, so the table is never loaded into memory (ОЗУ). True = on.
# Since 2026-11-10 it keeps only active collateral and summary columns (process.py), so
# it is light enough to be on. After changing it: sudo systemctl restart gunicorn.
ENABLED = True

# Who may delete saved days: False = anyone who can open the page,
# True = only users with «staff status» in the Django admin.
ONLY_STAFF_DELETES = False


def switchable(view):
    """While ENABLED is False the view does nothing heavy: it only says the app is off."""
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not ENABLED:
            return render(request, "collateral/page.html", {"off": True}, status=503)
        return view(request, *args, **kwargs)
    return wrapper


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


@switchable
def home(request, error=None):
    """The main page: the newest saved file (or the clicked one) with the chosen filters."""
    day = chosen_day(request)
    saved = process.saved_days()
    context = {"saved": saved, "error": error, "today": date.today(),
               "check_accounts": queries.CHECK_ACCOUNTS,
               "saved_total": f"{sum(s['bytes'] for s in saved) / 1e6:.1f} МБ"}
    if day is None:                      # nothing downloaded yet: only the «Обновить» button
        return render(request, "collateral/page.html", context)

    filters = read_filters(request)
    context.update(process.build_page(process.read_day(day), day, filters))
    context.update({
        "day": day,
        "updated": process.updated_at(day),
        "filters": filters,
        "link": address(day, filters),          # the current view, to add one more filter
        "crumbs": breadcrumbs(day, filters),
    })
    return render(request, "collateral/page.html", context)


@switchable
@require_POST
def refresh(request):
    """«Обновить из базы»: run the three queries now, save as today's file, show it."""
    try:
        process.save_today()
    except Exception as error:          # no database, wrong table name, no pyarrow ...
        return home(request, error=f"Не удалось загрузить данные из базы: {error}")
    return redirect("collateral")


@switchable
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


@switchable
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


@switchable
def accounts_excel(request):
    """The 945xx accounts with a balance and no collateral deal, as .xlsx."""
    day = chosen_day(request)
    if day is None or process.accounts_of(day) is None:
        raise Http404("Счета 945xx за этот день не загружены")
    table = process.orphans_excel(process.accounts_of(day))
    return download(table, f"accounts_945_{day.isoformat()}", "Счета без залога")


@switchable
def excel(request):
    """The current view as a summary (Итого + every card, every row of it): never a row per deal."""
    day = chosen_day(request)
    if day is None:
        raise Http404("Данные ещё не загружены")
    table = process.summary_excel(process.read_day(day), read_filters(request))
    return download(table, f"collateral_summary_{day.isoformat()}", "Сводка")


def download(table, name, sheet):
    """.xlsx, or .csv when the table is too big to write as Excel in time (process.EXCEL_MAX_CELLS)."""
    if table.size > process.EXCEL_MAX_CELLS:
        response = HttpResponse(process.to_csv(table), content_type="text/csv; charset=utf-8")
        response["Content-Disposition"] = f'attachment; filename="{name}.csv"'
        return response
    response = HttpResponse(process.to_xlsx(table, sheet),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f'attachment; filename="{name}.xlsx"'
    return response


@switchable
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
