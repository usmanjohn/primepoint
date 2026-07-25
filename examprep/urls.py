from django.urls import path
from . import views

urlpatterns = [
    path('',                                          views.examprep_home, name='examprep_home'),
    # Drills come before the skill routes: 'drills' would otherwise be read
    # as a skill slug by <slug:skill>.
    path('<slug:track_slug>/drills/',                 views.drill_list,    name='examprep_drills'),
    path('<slug:track_slug>/drills/<int:pk>/',        views.drill_detail,  name='examprep_drill'),
    path('<slug:track_slug>/drills/<int:pk>/finish/', views.drill_finish,  name='examprep_drill_finish'),
    path('<slug:track_slug>/',                        views.track_detail,  name='examprep_track'),
    path('<slug:track_slug>/<slug:skill>/',           views.skill_detail,  name='examprep_skill'),
    path('<slug:track_slug>/<slug:skill>/<slug:slug>/edit/', views.lesson_edit, name='examprep_lesson_edit'),
    path('<slug:track_slug>/<slug:skill>/<slug:slug>/finish/', views.lesson_finish, name='examprep_lesson_finish'),
    path('<slug:track_slug>/<slug:skill>/<slug:slug>/', views.lesson_detail, name='examprep_lesson'),
]
