from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="vintage"),
    path("rebuild/", views.rebuild, name="vintage-rebuild"),
    path("excel/", views.excel, name="vintage-excel"),
    path("plan/", views.plan, name="vintage-plan"),
]
