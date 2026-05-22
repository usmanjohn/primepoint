from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_home, name='games_home'),
    path('number-guess/', views.number_guess, name='number_guess'),
    path('crossword/', views.crossword_list, name='crossword_list'),
    path('crossword/<int:pk>/', views.crossword_play, name='crossword_play'),
]
