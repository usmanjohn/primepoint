from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('set-language/', views.set_language, name='set_language'),
    path('search/', views.search, name='search'),
]

 