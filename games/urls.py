from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_home, name='games_home'),
    path('number-guess/', views.number_guess, name='number_guess'),
    path('crossword/', views.crossword_list, name='crossword_list'),
    path('crossword/<int:pk>/', views.crossword_play, name='crossword_play'),
    path('crossword/<int:pk>/edit/', views.crossword_edit, name='crossword_edit'),
    path('crossword/<int:pk>/print/', views.crossword_print, name='crossword_print'),
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
    # Odd One Out
    path('oddoneout/', views.oddoneout_list, name='oddoneout_list'),
    path('oddoneout/create/', views.oddoneout_create, name='oddoneout_create'),
    path('oddoneout/<int:pk>/manage/', views.oddoneout_manage, name='oddoneout_manage'),
    path('oddoneout/<int:pk>/', views.oddoneout_play, name='oddoneout_play'),
    path('oddoneout/<int:pk>/check/', views.oddoneout_check, name='oddoneout_check'),
    # Word Search
    path('wordsearch/', views.wordsearch_list, name='wordsearch_list'),
    path('wordsearch/<int:pk>/', views.wordsearch_play, name='wordsearch_play'),
    # English Crossword
    path('english-crossword/', views.english_crossword_list, name='english_crossword_list'),
    path('english-crossword/<int:pk>/', views.english_crossword_play, name='english_crossword_play'),
    path('english-crossword/<int:pk>/edit/', views.english_crossword_edit, name='english_crossword_edit'),
    path('english-crossword/<int:pk>/print/', views.english_crossword_print, name='english_crossword_print'),
    # Word Order Chaos
    path('wordorder/', views.wordorder_list, name='wordorder_list'),
    path('wordorder/create/', views.wordorder_create, name='wordorder_create'),
    path('wordorder/<int:pk>/', views.wordorder_play, name='wordorder_play'),
    path('wordorder/<int:pk>/check/', views.wordorder_check, name='wordorder_check'),
    # Target Number
    path('target-number/', views.target_number, name='target_number'),
    path('target-number/check/', views.target_number_check, name='target_number_check'),
    # Math Championship
    path('championship/', views.mathchamp_home, name='mathchamp_home'),
    path('championship/play/', views.mathchamp_play, name='mathchamp_play'),
    # Math Square (Cross-Math)
    path('math-square/', views.mathsquare_list, name='mathsquare_list'),
    path('math-square/create/', views.mathsquare_create, name='mathsquare_create'),
    path('math-square/<int:pk>/', views.mathsquare_play, name='mathsquare_play'),
    path('math-square/<int:pk>/edit/', views.mathsquare_edit, name='mathsquare_edit'),
    path('math-square/<int:pk>/print/', views.mathsquare_print, name='mathsquare_print'),
]
