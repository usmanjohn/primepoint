from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_home, name='games_home'),
    path('number-guess/', views.number_guess, name='number_guess'),
    path('crossword/', views.crossword_list, name='crossword_list'),
    path('crossword/<int:pk>/', views.crossword_play, name='crossword_play'),
    path('crossword/<int:pk>/edit/', views.crossword_edit, name='crossword_edit'),
    # Code Breaker
    path('codebreaker/', views.codebreaker_list, name='codebreaker_list'),
    path('codebreaker/create/', views.codebreaker_create, name='codebreaker_create'),
    path('codebreaker/<int:pk>/', views.codebreaker_play, name='codebreaker_play'),
    path('codebreaker/<int:pk>/check/', views.codebreaker_check, name='codebreaker_check'),
    # Prime Climb Grid
    path('primeclimb/', views.primeclimb_list, name='primeclimb_list'),
    path('primeclimb/create/', views.primeclimb_create, name='primeclimb_create'),
    path('primeclimb/<int:pk>/', views.primeclimb_play, name='primeclimb_play'),
    path('primeclimb/<int:pk>/check/', views.primeclimb_check, name='primeclimb_check'),
    # Sorting Race
    path('sortingrace/', views.sortingrace_list, name='sortingrace_list'),
    path('sortingrace/create/', views.sortingrace_create, name='sortingrace_create'),
    path('sortingrace/<int:pk>/', views.sortingrace_play, name='sortingrace_play'),
    path('sortingrace/<int:pk>/check/', views.sortingrace_check, name='sortingrace_check'),
    # Word Order Chaos
    path('wordorder/', views.wordorder_list, name='wordorder_list'),
    path('wordorder/create/', views.wordorder_create, name='wordorder_create'),
    path('wordorder/<int:pk>/', views.wordorder_play, name='wordorder_play'),
    path('wordorder/<int:pk>/check/', views.wordorder_check, name='wordorder_check'),
]
