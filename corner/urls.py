from django.urls import path
from . import views

urlpatterns = [
    path('',                              views.corner_home,              name='corner_home'),
    path('templates/',                    views.corner_templates,         name='corner_templates'),
    path('templates/<int:pk>/',           views.corner_template_detail,   name='corner_template_detail'),
    path('templates/<int:pk>/download/',  views.corner_template_download, name='corner_template_download'),
    path('<slug:subject_slug>/',          views.corner_subject,           name='corner_subject'),
    path('<slug:subject_slug>/<slug:collection_slug>/',                      views.corner_collection,   name='corner_collection'),
    path('<slug:subject_slug>/<slug:collection_slug>/<slug:slug>/edit/',     views.corner_story_edit,   name='corner_story_edit'),
    path('<slug:subject_slug>/<slug:collection_slug>/<slug:slug>/finish/',   views.corner_story_finish, name='corner_story_finish'),
    path('<slug:subject_slug>/<slug:collection_slug>/<slug:slug>/',          views.corner_story,        name='corner_story'),
]
