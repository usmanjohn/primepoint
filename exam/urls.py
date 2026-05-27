from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('<int:pk>/', views.exam_detail, name='exam_detail'),
    path('<int:pk>/start/', views.start_exam, name='start_exam'),
    path('attempt/<int:attempt_id>/', views.take_section, name='take_section'),
    path('attempt/<int:attempt_id>/submit/', views.submit_section, name='submit_section'),
    path('attempt/<int:attempt_id>/result/', views.exam_result, name='exam_result'),
]
