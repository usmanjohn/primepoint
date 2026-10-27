"""
The pages of the vintage app. Every view is short: it reads the address, asks process.py
for the numbers and gives them to a template.

    /vintage/?kind=dpd90&measure=amount&seg=all
                                            the analysis (kind: dpd30, dpd60, dpd90, npl;
                                            measure: amount, count; seg: all or a passport)
    /vintage/plan/?kind=dpd90&lending=…     the business plan for the next 12 months
    /vintage/excel/?kind=…&measure=…        everything of the analysis in Excel
    /vintage/rebuild/  (POST)               starts `manage.py build_vintage` in its own process

The heavy work (tens of millions of rows) is never done inside a page: the build runs as
its own process and the pages read only its small results.
"""
import json
import os
import subprocess
import sys

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from . import process


def chosen(request):
    kind = request.GET.get("kind")
    measure = request.GET.get("measure")
    return (kind if kind in process.KINDS else "dpd90",
            measure if measure in process.MEASURES else "amount")


def chosen_seg(request, res):
    """?seg=vtorichka if that passport exists in the results, otherwise all passports."""
    seg = request.GET.get("seg")
    keys = [s["key"] for s in process.segments(res)] if res else []
    return seg if seg in keys else process.ALL


def pid_alive(pid):
    if not pid or os.name == "nt":          # on Windows os.kill(pid, 0) would KILL the process
        return True
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def build_status():
    """{'running': …, 'started': …, 'error': …} from status.json; a dead 'running' becomes an error."""
    try:
        status = json.loads(process.STATUS_FILE.read_text())
    except (FileNotFoundError, ValueError):
        return {}
    if status.get("running") and not pid_alive(status.get("pid")):
        status = {"running": False, "started": status.get("started"),
                  "error": "расчёт остановлен системой (часто — нехватка памяти). Смотрите datasets/vintage/build.log"}
    return status


@login_required
def home(request):
    kind, measure = chosen(request)
    group = process.KINDS[kind]["group"]
    res = process.results()
    seg = chosen_seg(request, res)
    context = {"status": build_status(), "kind": kind, "measure": measure, "seg": seg,
               "kinds": process.KINDS, "measures": process.MEASURES, "input_dir": process.INPUT_DIR,
               "label": process.KINDS[kind]["label"], "measure_name": process.MEASURES[measure], "res": res}
    if res:
        vintages, R, weight = process.matrix(res, kind, measure, seg)
        steps, reached = process.average_steps(R, weight)
        P, proj = process.projected(R, steps)
        mobs, rows = process.triangle_table(vintages, R, P, proj)
        found, ref = process.insights(vintages, R, weight, steps, kind, measure)
        meta = res["meta"]
        context.update({
            "meta": meta, "mobs": mobs, "rows": rows, "insights": found, "ref": ref,
            "curves": process.curves_svg(vintages, R, weight, steps, res["meta"]["last_month"]),
            "transitions": process.transitions_table(res, group, measure, seg),
            "early": process.early_signal(res, "npl" if group == "npl" else "dpd90", seg),
            "comparison": process.compare(res, kind, measure),
            "segments": [dict(s, loans_text=f"{s['loans']:,}".replace(",", " ")) for s in process.segments(res)],
            "seg_label": process.segment_label(res, seg),
            "season": process.seasonality(vintages, R, weight, ref),
            "vintage_count": len(vintages),
            "loans": f"{process.loans_in_vintages(res, seg):,}".replace(",", " "),
            "migration_months": process.MIGRATION_MONTHS, "recent": process.RECENT_VINTAGES,
            "early_mob": process.EARLY_MOB, "late_mob": process.LATE_MOB,
        })
    return render(request, "vintage/page.html", context)


@login_required
@require_POST
def rebuild(request):
    if build_status().get("running"):
        messages.info(request, "Расчёт уже идёт.")
        return redirect("vintage")
    process.BASE.mkdir(parents=True, exist_ok=True)
    manage = os.path.join(settings.BASE_DIR, "manage.py")
    log = open(process.LOG_FILE, "w")
    options = {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP} if os.name == "nt" else {"start_new_session": True}
    proc = subprocess.Popen([sys.executable, manage, "build_vintage"], cwd=settings.BASE_DIR,
                            stdout=log, stderr=subprocess.STDOUT, **options)
    process.STATUS_FILE.write_text(json.dumps({"running": True, "pid": proc.pid, "started": "только что"}))
    messages.success(request, "Расчёт запущен. Страница обновится сама, когда он закончится.")
    return redirect("vintage")


@login_required
def excel(request):
    kind, measure = chosen(request)
    res = process.results()
    if not res:
        return redirect("vintage")
    seg = chosen_seg(request, res)
    data = process.xlsx(process.excel_sheets(res, kind, measure, seg))
    name = f"vintage_{seg}_{kind}_{measure}_{res['meta']['last_month']:%Y-%m}.xlsx"
    response = HttpResponse(data, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f'attachment; filename="{name}"'
    return response


def number(text, default):
    """'36 599,5' or '36599.5' → 36599.5; anything else → default."""
    try:
        return float(str(text).replace(" ", "").replace("\xa0", "").replace(",", "."))
    except ValueError:
        return default


@login_required
def plan(request):
    kind = request.GET.get("kind") if request.GET.get("kind") in ("dpd90", "npl") else "dpd90"
    res = process.results()
    if not res:
        return redirect("vintage")
    seg = chosen_seg(request, res)
    default = process.default_lending(res, kind, seg) / process.AMOUNT_DIVISOR
    lending = max(0.0, number(request.GET.get("lending", ""), default))
    growth = number(request.GET.get("growth", ""), 0.0)
    rows = process.plan(res, kind, lending * process.AMOUNT_DIVISOR, growth / 100, seg)
    stock = process.markov(res, process.KINDS[kind]["group"], lending * process.AMOUNT_DIVISOR, growth / 100, seg)

    if request.GET.get("excel"):
        sheets = [("План", ["Месяц", "Выдача", "Новые из текущего портфеля", "Новые из новой выдачи", "Всего", "Накоплено"],
                   [[r["month"], r["lending"], r["book"], r["new"], r["total"], r["cum"]] for r in rows]),
                  ("Доля в портфеле", ["Месяц", "Портфель", "Плохой остаток", "Доля", "Факт/прогноз"],
                   [[r["month"], r["total"], r["bad"], r["share"], "факт" if r["fact"] else "прогноз"] for r in stock])]
        response = HttpResponse(process.xlsx(sheets),
                                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = f'attachment; filename="vintage_plan_{seg}_{kind}.xlsx"'
        return response

    top = max([r["total"] for r in rows] + [1])
    shown = [{"month": f"{r['month']:%m.%Y}", "lending": process.money(r["lending"]), "book": process.money(r["book"]),
              "new": process.money(r["new"]), "total": process.money(r["total"]), "cum": process.money(r["cum"]),
              "bar_book": round(r["book"] / top * 100), "bar_new": round(r["new"] / top * 100)} for r in rows]
    year = sum(r["total"] for r in rows)
    lent = sum(r["lending"] for r in rows)
    return render(request, "vintage/plan.html", {
        "kind": kind, "label": process.KINDS[kind]["label"], "meta": res["meta"], "rows": shown,
        "seg": seg, "seg_label": process.segment_label(res, seg), "segments": process.segments(res),
        "lending": process.num(lending, 1), "default": process.num(default, 1), "growth": process.num(growth, 1),
        "unit": process.AMOUNT_UNIT, "months": process.PLAN_MONTHS,
        "year_total": process.money(year), "year_lent": process.money(lent),
        "year_book": process.money(sum(r["book"] for r in rows)), "year_new": process.money(sum(r["new"] for r in rows)),
        "stock": [{"month": f"{r['month']:%m.%Y}", "share": process.pct(r["share"]), "bad": process.money(r["bad"]),
                   "total": process.money(r["total"]), "fact": r["fact"]} for r in stock],
        "query": request.GET.urlencode(),
    })
