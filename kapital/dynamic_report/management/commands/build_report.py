"""
Same engine from the command line — for cron, or when you'd rather not wait
in a browser.

    python manage.py build_report --from 202301 --to 202609 --selected 202609
"""
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from dynamic_report import process
from dynamic_report.models import ReportRun


class Command(BaseCommand):
    help = "Построить отчёт по портфелю из месячных parquet-файлов."

    def add_arguments(self, p):
        p.add_argument("--from", dest="pfrom", type=int, default=None)
        p.add_argument("--to", dest="pto", type=int, default=None)
        p.add_argument("--selected", type=int, default=None)

    def handle(self, *a, **o):
        data = Path(settings.BASE_DIR) / "datasets" / "dynamics" / "yearly"
        outd = Path(settings.BASE_DIR) / "datasets" / "dynamics" / "report"
        run = ReportRun.objects.create(period_from=o["pfrom"], period_to=o["pto"],
                                       selected_period=o["selected"],
                                       status=ReportRun.RUNNING, created_by="cli")
        try:
            out = outd / f"report_{o['selected'] or 'last'}_{run.pk}.html"
            stats = process.run(data, out, o["pfrom"], o["pto"], o["selected"],
                                progress=lambda m: self.stdout.write(f"  {m}"))
            run.status, run.html_path, run.stats = run.DONE, str(out), stats
            run.period_from, run.period_to = stats["period_from"], stats["period_to"]
            run.selected_period = stats["selected_period"]
            run.finished_at = timezone.now(); run.save()
            self.stdout.write(self.style.SUCCESS(f"готово за {run.seconds}s -> {out}"))
        except Exception as exc:
            run.status, run.error = run.FAILED, str(exc)
            run.finished_at = timezone.now(); run.save()
            raise
