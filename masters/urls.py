from django.urls import path
from . import views

urlpatterns = [
    path('', views.master_list, name='masters-home'),
    path('create/', views.master_create, name='masters-create'),
    path('<int:master_id>/', views.master_detail, name='masters-detail'),
    path('update/<int:pk>/', views.master_update, name='update-master'),
    path('delete/<int:pk>/', views.master_delete, name='delete-master'),
]
