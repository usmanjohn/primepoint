from django.urls import path
from . import views

urlpatterns = [
    path("", views.page, name="report-page"),
    path("start/", views.start, name="report-start"),
    path("status/<int:pk>/", views.status, name="report-status"),
    path("view/<int:pk>/", views.view_report, name="report-view"),
    path("download/<int:pk>/", views.download_report, name="report-download"),
    path("delete/<int:pk>/", views.delete_report, name="report-delete"),
]
