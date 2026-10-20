from django.urls import path
from . import views

urlpatterns = [
    path("", views.page, name="client-portfolio"),
    path("excel/", views.excel, name="client-portfolio-excel"),
]
