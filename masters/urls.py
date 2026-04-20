from django.urls import path
from . import views

urlpatterns = [
    path('', views.MasterListView.as_view(), name='masters-home'),
    path('list/', views.MasterListView.as_view(), name='masters-list'),
    path('create/', views.MasterCreateView.as_view(), name='masters-create'),
    path('<int:master_id>/', views.MasterDetailView.as_view(), name='masters-detail'),
    path('update/<int:pk>/', views.MasterUpdateView.as_view(), name='update-master'),
    path('delete/<int:pk>/', views.MasterDeleteView.as_view(), name='delete-master'),
]
