from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="fast-search"),
    path("<str:name>/", views.report, name="fast-search-report"),
]
