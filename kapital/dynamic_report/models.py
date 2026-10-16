"""
One model. It is a job record, not a data store — the data lives in parquet.

Why a model at all, when the HTML could just be written to disk: a run takes
minutes, so the browser cannot wait for it. The row is how the page polls for
progress, and how you find last month's report without regenerating it.
"""
from __future__ import annotations

from django.db import models


class ReportRun(models.Model):
    PENDING, RUNNING, DONE, FAILED = "pending", "running", "done", "failed"
    STATUS = [(PENDING, "в очереди"), (RUNNING, "выполняется"),
              (DONE, "готов"), (FAILED, "ошибка")]

    # request parameters
    period_from     = models.IntegerField(null=True, blank=True)
    period_to       = models.IntegerField(null=True, blank=True)
    selected_period = models.IntegerField(null=True, blank=True)

    # identity of (parameters + input files) — lets an identical request reuse
    # a finished report instead of spending minutes rebuilding it
    fingerprint = models.CharField(max_length=32, blank=True, db_index=True)

    # progress
    status  = models.CharField(max_length=10, choices=STATUS, default=PENDING)
    step    = models.CharField(max_length=120, blank=True)
    error   = models.TextField(blank=True)

    # result
    html_path = models.CharField(max_length=500, blank=True)
    stats     = models.JSONField(default=dict, blank=True)

    created_at  = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    created_by  = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["-created_at"]),
                   models.Index(fields=["status"])]

    def __str__(self):
        return f"#{self.pk} {self.selected_period or 'последний'} [{self.status}]"

    @property
    def seconds(self):
        """Run time; for a job still running, the time so far."""
        from django.utils import timezone
        end = self.finished_at or (timezone.now() if self.is_active else self.created_at)
        return round((end - self.created_at).total_seconds(), 1)

    @property
    def is_active(self):
        return self.status in (self.PENDING, self.RUNNING)
