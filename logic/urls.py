from django.urls import path
from . import views

urlpatterns = [
    path('',              views.logic_home,        name='logic_home'),
    path('hall/',         views.logic_leaderboard, name='logic_leaderboard'),
    path('my-answers/',   views.logic_my_answers,  name='logic_my_answers'),
    path('<slug:slug>/',  views.logic_puzzle,      name='logic_puzzle'),
]
