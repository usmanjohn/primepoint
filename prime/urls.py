from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('help/', views.help_page, name='help'),
    path('search/', views.search, name='search'),
    path('study-subjects/', views.set_study_subjects, name='set_study_subjects'),
    path('sw.js', views.service_worker, name='service_worker'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]

 