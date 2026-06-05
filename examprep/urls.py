from django.urls import path
from . import views

urlpatterns = [
    path('',                                  views.examprep_home, name='examprep_home'),
    path('<slug:slug>/',                      views.track_detail,  name='examprep_track'),
    path('<slug:track_slug>/<slug:slug>/',    views.lesson_detail, name='examprep_lesson'),
]
