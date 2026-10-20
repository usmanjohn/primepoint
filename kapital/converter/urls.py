from django.urls import path
from . import views

urlpatterns = [
    path("", views.page, name="converter"),
    path("run/<str:tool>/", views.run, name="converter-run"),
]
