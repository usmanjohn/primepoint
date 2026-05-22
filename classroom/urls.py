from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    # Classroom CRUD
    path('', views.classroom_list, name='list'),
    path('create/', views.classroom_create, name='create'),
    path('<int:pk>/', views.classroom_detail, name='detail'),
    path('<int:pk>/edit/', views.classroom_edit, name='edit'),
    path('<int:pk>/delete/', views.classroom_delete, name='delete'),
    path('<int:pk>/manage/', views.classroom_manage, name='manage'),

    # Lesson CRUD
    path('<int:classroom_pk>/lessons/create/', views.lesson_create, name='lesson_create'),
    path('<int:classroom_pk>/lessons/<int:lesson_pk>/', views.lesson_detail, name='lesson_detail'),
    path('<int:classroom_pk>/lessons/<int:lesson_pk>/edit/', views.lesson_edit, name='lesson_edit'),
    path('<int:classroom_pk>/lessons/<int:lesson_pk>/delete/', views.lesson_delete, name='lesson_delete'),

    # Lesson Notes
    path('<int:classroom_pk>/lessons/<int:lesson_pk>/notes/upload/', views.lesson_note_upload, name='note_upload'),
    path('<int:classroom_pk>/lessons/<int:lesson_pk>/notes/<int:note_pk>/delete/', views.lesson_note_delete, name='note_delete'),

    # Classroom Discussion
    path('<int:classroom_pk>/discussion/', views.discussion_list, name='discussion_list'),
    path('<int:classroom_pk>/discussion/create/', views.discussion_create, name='discussion_create'),
    path('<int:classroom_pk>/discussion/<int:thread_pk>/', views.discussion_thread, name='discussion_thread'),
    path('<int:classroom_pk>/discussion/<int:thread_pk>/delete/', views.discussion_delete, name='discussion_delete'),
]
