"""
Three views: the form, a status endpoint the page polls, and the report itself.

The one thing that matters here: run() NEVER happens inside the web server.
Not in the request, and not in a thread of the gunicorn worker either: a full-history
run needs gigabytes, and when the out-of-memory killer took the worker, the report, the
status page and the row's status went with it. The POST starts a separate process
(jobs.launch → manage.py build_report --run-id N), returns at once with the job id,
and the page polls.
"""
from __future__ import annotations

import re
from pathlib import Path

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from . import jobs, process
from .models import ReportRun

BASE_DIR = Path(settings.BASE_DIR)
DATA_DIR = BASE_DIR / "datasets" / "dynamics" / "yearly"
OUT_DIR = jobs.OUT_DIR


def _period_choices():
    # value is a STRING on purpose: with USE_THOUSAND_SEPARATOR the template would print
    # the int 202508 as "202 508", the form would send that back, and the date was lost.
    out = []
    for p in process.available_periods(DATA_DIR):
        out.append({"value": str(p), "label": process.plabel_full(p)})
    return out


def _period_int(v):
    """'202508', '202 508', '202,508' -> 202508; anything else -> None."""
    digits = re.sub(r"\D", "", str(v or ""))
    return int(digits) if len(digits) == 6 else None


def _is_admin(request):
    """Admins (staff or superuser) may delete reports; everyone else only opens and downloads."""
    user = getattr(request, "user", None)
    return bool(getattr(user, "is_staff", False) or getattr(user, "is_superuser", False))


def _plabel(p):
    return process.plabel_full(p) if p else None


def page(request):
    """The form plus the history of previous runs."""
    jobs.reap_stale()                        # no row stays «выполняется» after its process died
    periods = _period_choices()
    return render(request, "dynamic_report/page.html", {
        "periods": periods,
        "latest": periods[-1]["value"] if periods else None,
        "latest_label": periods[-1]["label"] if periods else None,
        "runs": _with_labels(ReportRun.objects.all()[:15]),
        "n_files": len(periods),
        "n_done": ReportRun.objects.filter(status=ReportRun.DONE).count(),
        "is_admin": _is_admin(request),
    })


def _with_labels(runs):
    """History table: «сен 2025», never a raw (and possibly '202 508'-formatted) int."""
    runs = list(runs)
    for r in runs:
        r.from_label, r.to_label, r.sel_label = (_plabel(r.period_from), _plabel(r.period_to),
                                                 _plabel(r.selected_period))
    return runs


@require_POST
def start(request):
    pf, pt, sel = (_period_int(request.POST.get(k))
                   for k in ("period_from", "period_to", "selected_period"))
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
                                 "cached": True, "params": _params(pf, pt, sel)})

        # the same report is already being built (e.g. the button was pressed again after the
        # page lost the connection): follow that one instead of starting a second copy
        jobs.reap_stale()
        active = (ReportRun.objects.filter(fingerprint=fp, status__in=[ReportRun.PENDING, ReportRun.RUNNING])
                  .order_by("-created_at").first())
        if active:
            return JsonResponse({"id": active.pk, "status": active.status,
                                 "cached": False, "params": _params(pf, pt, sel)})

    run = ReportRun.objects.create(
        period_from=pf, period_to=pt, selected_period=sel,
        fingerprint=fp, created_by=username)
    try:
        jobs.launch(run)
    except Exception as exc:
        ReportRun.objects.filter(pk=run.pk).update(
            status=ReportRun.FAILED, error=f"не удалось запустить расчёт: {exc}", finished_at=timezone.now())
        return JsonResponse({"error": f"не удалось запустить расчёт: {exc}"}, status=500)
    return JsonResponse({"id": run.pk, "status": run.status, "cached": False,
                         "params": _params(pf, pt, sel)})


def _params(pf, pt, sel):
    """What the server actually understood — the page shows it, so a lost date is visible."""
    return (f"динамика {_plabel(pf) or 'с начала'} — {_plabel(pt) or 'до конца'}, "
            f"структура на {_plabel(sel) or 'последнюю дату'}")


@require_GET
def status(request, pk: int):
    r = get_object_or_404(ReportRun, pk=pk)
    if r.is_active:
        jobs.reap_stale()
        r.refresh_from_db()
    return JsonResponse({
        "id": r.pk, "status": r.status, "step": r.step, "error": r.error,
        "seconds": r.seconds, "stats": r.stats,
        "params": _params(r.period_from, r.period_to, r.selected_period),
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


@require_POST
def delete_report(request, pk: int):
    """Admin only: remove a report row and its HTML file. A running job cannot be deleted."""
    if not _is_admin(request):
        raise PermissionDenied("удалять отчёты может только администратор")
    r = get_object_or_404(ReportRun, pk=pk)
    if r.is_active:
        return redirect("report-page")
    jobs.log_path(r.pk).unlink(missing_ok=True)
    if r.html_path:
        f = Path(r.html_path)
        # never touch a file outside the reports folder, whatever the row says
        if f.exists() and OUT_DIR.resolve() in f.resolve().parents:
            f.unlink()
    r.delete()
    return redirect("report-page")
