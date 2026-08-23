from django.urls import path
from . import views

urlpatterns = [
    # The pupil's inbox — everything due, from every classroom.
    path('', views.my_homework, name='my_homework'),

    # Setting homework moved into the classroom in August 2026. These stay as
    # redirects: they are bookmarked, and linked from older profile pages.
    path('manage/', views.manage_homework, name='manage_homework'),
    path('create/', views.create_homework, name='create_homework'),
    path('groups/', views.manage_groups, name='manage_groups'),
    path('<int:pk>/', views.homework_detail, name='homework_detail'),
]
