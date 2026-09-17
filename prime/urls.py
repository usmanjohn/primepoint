from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('help/', views.help_page, name='help'),
    path('search/', views.search, name='search'),
    path('progress/', views.progress, name='progress'),

    # The hand-out kit — printable marketing pieces, open to everyone.
    path('kit/card/', views.kit_card, name='kit_card'),
    path('kit/card/sheet/', views.kit_card_sheet, name='kit_card_sheet'),
    path('kit/flyer/', views.kit_flyer, name='kit_flyer'),
    path('study-subjects/', views.set_study_subjects, name='set_study_subjects'),
    path('sw.js', views.service_worker, name='service_worker'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]

 