from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_home, name='games_home'),
    path('number-guess/', views.number_guess, name='number_guess'),
]
