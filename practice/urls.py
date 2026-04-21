from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('',views.practice_list, name='practice_list'),
    path('<int:pk>/',views.practice_detail,  name='practice_detail'),

    # Attempt flow
    path('<int:pk>/start/',views.start_practice,   name='start_practice'),
    path('attempt/<int:attempt_id>/', views.take_practice, name='take_practice'),
    path('attempt/<int:attempt_id>/finish/', views.finish_practice, name='finish_practice'),
    path('attempt/<int:attempt_id>/result/', views.practice_result,  name='practice_result'),

    # Master management
    path('manage/', views.manage_practices, name='manage_practices'),
    path('manage/<int:pk>/toggle/', views.toggle_publish, name='toggle_publish'),
]