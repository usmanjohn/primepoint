from django.urls import path
from . import views

urlpatterns = [
    path('',                                          views.examprep_home, name='examprep_home'),
    path('<slug:track_slug>/',                        views.track_detail,  name='examprep_track'),
    path('<slug:track_slug>/<slug:skill>/',           views.skill_redirect, name='examprep_skill'),
    path('<slug:track_slug>/<slug:skill>/<slug:slug>/', views.lesson_detail, name='examprep_lesson'),
]
