from django.contrib import admin
from .models import ReportRun


@admin.register(ReportRun)
class ReportRunAdmin(admin.ModelAdmin):
    list_display = ("id", "selected_period", "period_from", "period_to",
                    "status", "step", "seconds", "created_at")
    list_filter = ("status",)
    readonly_fields = ("stats", "error", "created_at", "finished_at")
