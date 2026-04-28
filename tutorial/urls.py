from django.urls import path
from . import views

urlpatterns = [
    path('',                 views.tutorial_list,   name='tutorial_list'),
    path('create/',          views.tutorial_create, name='tutorial_create'),
    path('<int:pk>/',        views.tutorial_detail, name='tutorial_detail'),
    path('<int:pk>/react/',  views.tutorial_react,  name='tutorial_react'),
    path('<int:pk>/edit/',   views.tutorial_edit,   name='tutorial_edit'),
    path('<int:pk>/delete/', views.tutorial_delete, name='tutorial_delete'),
]
