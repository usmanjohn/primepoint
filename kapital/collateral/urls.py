from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="collateral"),
    path("refresh/", views.refresh, name="collateral-refresh"),
    path("delete/", views.delete, name="collateral-delete"),
    path("accounts/", views.accounts, name="collateral-accounts"),
    path("accounts/excel/", views.accounts_excel, name="collateral-accounts-excel"),
    path("excel/", views.excel, name="collateral-excel"),
    path("params/", views.params, name="collateral-params"),
]
