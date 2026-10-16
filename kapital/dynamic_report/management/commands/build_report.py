"""
Builds one report. The web page starts it as its own process (see jobs.py) with --run-id;
you can also run it by hand — for cron, or when you'd rather not wait in a browser:

    python manage.py build_report --from 202301 --to 202609 --selected 202609

Only one report builds at a time on the server: a second one waits («в очереди») until the
first is finished.
"""
import os
import traceback
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from dynamic_report import jobs, process
from dynamic_report.models import ReportRun


class Command(BaseCommand):
    help = "Построить отчёт по портфелю из месячных parquet-файлов."

    def add_arguments(self, p):
        p.add_argument("--run-id", type=int, default=None,
                       help="строка ReportRun, созданная веб-страницей")
        p.add_argument("--from", dest="pfrom", type=int, default=None)
        p.add_argument("--to", dest="pto", type=int, default=None)
        p.add_argument("--selected", type=int, default=None)

    def handle(self, *a, **o):
        data = Path(settings.BASE_DIR) / "datasets" / "dynamics" / "yearly"
        if o["run_id"]:
            run = ReportRun.objects.get(pk=o["run_id"])
        else:
            run = ReportRun.objects.create(period_from=o["pfrom"], period_to=o["pto"],
                                           selected_period=o["selected"], created_by="cli")
        rows = ReportRun.objects.filter(pk=run.pk)
        rows.update(stats={"pid": os.getpid()})          # lets the page tell a dead job from a live one

        def progress(msg):
            rows.update(step=str(msg)[:120])
            self.stdout.write(f"  {msg}")
            self.stdout.flush()

        def waiting():
            rows.update(status=ReportRun.PENDING, step="ожидание: другой отчёт выполняется")
            self.stdout.write("  ожидание: другой отчёт выполняется")
            self.stdout.flush()

        with jobs.build_lock(on_wait=waiting):
            rows.update(status=ReportRun.RUNNING, step="запуск")
            try:
                out = jobs.OUT_DIR / f"report_{run.selected_period or 'last'}_{run.pk}.html"
                stats = process.run(data, out, period_from=run.period_from, period_to=run.period_to,
                                    selected_period=run.selected_period, progress=progress)
            except Exception as exc:
                rows.update(status=ReportRun.FAILED, step="", finished_at=timezone.now(),
                            error=f"{type(exc).__name__}: {exc}\n\n{traceback.format_exc()[-2000:]}")
                raise CommandError(f"{type(exc).__name__}: {exc}")

        run.refresh_from_db()
        run.status, run.step = ReportRun.DONE, "готово"
        run.html_path, run.stats = str(out), stats
        run.period_from, run.period_to = stats["period_from"], stats["period_to"]
        run.selected_period = stats["selected_period"]
        run.finished_at = timezone.now()
        run.save()
        jobs.log_path(run.pk).unlink(missing_ok=True)    # the log is only kept for failed runs
        self.stdout.write(self.style.SUCCESS(f"готово за {run.seconds}s -> {out}"))
