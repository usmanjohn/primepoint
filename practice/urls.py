from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='practice-home'),
    path('test/<int:pk>/', views.practice_detail, name='practice-start'),
    path('results/<int:attempt_id>/', views.attempt_result, name='attempt-result'),
]
