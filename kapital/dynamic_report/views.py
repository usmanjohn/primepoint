"""
Three views: the form, a status endpoint the page polls, and the report itself.

The one thing that matters here: run() NEVER happens inside the request.
8M rows takes minutes — it would blow past the gunicorn timeout, hold a worker
the whole time, and give the user a dead browser tab. So the POST starts a
thread, returns immediately with a job id, and the page polls.
"""
from __future__ import annotations

import threading
import traceback
import datetime as dt
from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from . import process
from .models import ReportRun

BASE_DIR = Path(settings.BASE_DIR)
DATA_DIR = BASE_DIR / "datasets" / "dynamics" / "yearly"
OUT_DIR = BASE_DIR / "datasets" / "dynamics" / "report"

# Only one heavy job at a time. Two concurrent 8M-row runs will exhaust RAM on
# a modest server, and nobody needs two reports at once.
_LOCK = threading.Lock()


def _period_choices():
    out = []
    for p in process.available_periods(DATA_DIR):
        out.append({"value": p, "label": process.plabel_full(p)})
    return out


def _worker(run_id: int):
    """Runs in a background thread. Owns its own DB connections."""
    from django.db import connection

    run = ReportRun.objects.get(pk=run_id)
    if not _LOCK.acquire(blocking=False):
        run.status, run.step = ReportRun.PENDING, "ожидание: другой отчёт выполняется"
        run.save(update_fields=["status", "step"])
        _LOCK.acquire()                      # now wait for the other job

    try:
        run.status, run.step = ReportRun.RUNNING, "запуск"
        run.save(update_fields=["status", "step"])

        def progress(msg):
            ReportRun.objects.filter(pk=run_id).update(step=msg)

        out = OUT_DIR / (f"report_{run.selected_period or 'last'}"
                         f"_{run.pk}.html")
        stats = process.run(DATA_DIR, out,
                            period_from=run.period_from,
                            period_to=run.period_to,
                            selected_period=run.selected_period,
                            progress=progress)

        run.refresh_from_db()
        run.status, run.step = ReportRun.DONE, "готово"
        run.html_path, run.stats = str(out), stats
        run.period_from = stats["period_from"]
        run.period_to = stats["period_to"]
        run.selected_period = stats["selected_period"]
        run.finished_at = timezone.now()
        run.save()
    except Exception as exc:
        ReportRun.objects.filter(pk=run_id).update(
            status=ReportRun.FAILED, step="",
            error=f"{type(exc).__name__}: {exc}\n\n{traceback.format_exc()[-2000:]}",
            finished_at=timezone.now())
    finally:
        _LOCK.release()
        connection.close()                   # a thread must not leak its connection


def page(request):
    """The form plus the history of previous runs."""
    periods = _period_choices()
    return render(request, "dynamic_report/page.html", {
        "periods": periods,
        "latest": periods[-1]["value"] if periods else None,
        "latest_label": periods[-1]["label"] if periods else None,
        "runs": ReportRun.objects.all()[:15],
        "n_files": len(periods),
        "n_done": ReportRun.objects.filter(status=ReportRun.DONE).count(),
    })


@require_POST
def start(request):
    def as_int(name):
        v = (request.POST.get(name) or "").strip()
        return int(v) if v.isdigit() else None

    pf, pt, sel = as_int("period_from"), as_int("period_to"), as_int("selected_period")
    if pf and pt and pf > pt:
        return JsonResponse({"error": "начало периода позже конца"}, status=400)
    if sel and pf and sel < pf:
        return JsonResponse({"error": "выбранная дата вне диапазона"}, status=400)
    if sel and pt and sel > pt:
        return JsonResponse({"error": "выбранная дата вне диапазона"}, status=400)

    # getattr(request.user, ...) still evaluates request.user, which raises when
    # AuthenticationMiddleware is not installed. Go through request first.
    user = getattr(request, "user", None)
    username = (getattr(user, "username", "") or "")[:150]

    fp = process.run_fingerprint(str(DATA_DIR), pf, pt, sel)

    # Same parameters, same input files -> hand back the finished report.
    # The fingerprint includes every file's mtime and size, so uploading a new
    # month invalidates it automatically. "force" overrides for a manual rebuild.
    if request.POST.get("force") != "1":
        cached = (ReportRun.objects
                  .filter(fingerprint=fp, status=ReportRun.DONE)
                  .order_by("-created_at").first())
        if cached and cached.html_path and Path(cached.html_path).exists():
            return JsonResponse({"id": cached.pk, "status": cached.status,
                                 "cached": True})

    run = ReportRun.objects.create(
        period_from=pf, period_to=pt, selected_period=sel,
        fingerprint=fp, created_by=username)

    threading.Thread(target=_worker, args=(run.pk,), daemon=True).start()
    return JsonResponse({"id": run.pk, "status": run.status, "cached": False})


@require_GET
def status(request, pk: int):
    r = get_object_or_404(ReportRun, pk=pk)
    return JsonResponse({
        "id": r.pk, "status": r.status, "step": r.step, "error": r.error,
        "seconds": r.seconds, "stats": r.stats,
        "url": reverse("report-view", args=[r.pk]) if r.status == r.DONE else None,
    })


@require_GET
def view_report(request, pk: int):
    """Serve the generated HTML. Opens in a new tab from the form page."""
    r = get_object_or_404(ReportRun, pk=pk)
    if r.status != r.DONE or not r.html_path or not Path(r.html_path).exists():
        raise Http404("отчёт ещё не готов")
    return FileResponse(open(r.html_path, "rb"), content_type="text/html; charset=utf-8")


@require_GET
def download_report(request, pk: int):
    r = get_object_or_404(ReportRun, pk=pk)
    if r.status != r.DONE or not Path(r.html_path or "").exists():
        raise Http404("отчёт ещё не готов")
    name = f"portfel_{r.selected_period}.html"
    return FileResponse(open(r.html_path, "rb"), as_attachment=True, filename=name)
