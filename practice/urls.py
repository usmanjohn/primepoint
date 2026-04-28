from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.practice_list, name='practice_list'),
    path('<int:pk>/', views.practice_detail, name='practice_detail'),

    # Attempt flow
    path('<int:pk>/start/', views.start_practice, name='start_practice'),
    path('attempt/<int:attempt_id>/', views.take_practice, name='take_practice'),
    path('attempt/<int:attempt_id>/finish/', views.finish_practice, name='finish_practice'),
    path('attempt/<int:attempt_id>/result/', views.practice_result, name='practice_result'),

    # Master management — practice level
    path('manage/', views.manage_practices, name='manage_practices'),
    path('manage/<int:pk>/toggle/', views.toggle_publish, name='toggle_publish'),
    path('manage/<int:pk>/toggle-available/', views.toggle_available, name='toggle_available'),
    path('create/', views.create_practice, name='create_practice'),
    path('<int:pk>/edit/', views.edit_practice, name='edit_practice'),

    # Master — student results
    path('<int:pk>/attempts/', views.practice_attempts, name='practice_attempts'),
    path('attempt/<int:attempt_id>/review/', views.review_attempt, name='review_attempt'),

    # Master management — question level
    path('<int:pk>/questions/', views.manage_questions, name='manage_questions'),
    path('<int:pk>/questions/add/', views.add_question, name='add_question'),
    path('<int:pk>/questions/<int:qpk>/edit/', views.edit_question, name='edit_question'),
    path('<int:pk>/questions/<int:qpk>/delete/', views.delete_question, name='delete_question'),
]
