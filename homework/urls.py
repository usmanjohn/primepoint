from django.urls import path
from . import views

urlpatterns = [
    # Student
    path('', views.my_homework, name='my_homework'),

    # Master — homework CRUD
    path('manage/', views.manage_homework, name='manage_homework'),
    path('create/', views.create_homework, name='create_homework'),
    path('<int:pk>/', views.homework_detail, name='homework_detail'),
    path('<int:pk>/edit/', views.edit_homework, name='edit_homework'),
    path('<int:pk>/delete/', views.delete_homework, name='delete_homework'),
    path('<int:pk>/assign/', views.assign_homework, name='assign_homework'),

    # Master — groups
    path('groups/', views.manage_groups, name='manage_groups'),
    path('groups/create/', views.create_group, name='create_group'),
    path('groups/<int:gpk>/edit/', views.edit_group, name='edit_group'),
    path('groups/<int:gpk>/delete/', views.delete_group, name='delete_group'),
]
