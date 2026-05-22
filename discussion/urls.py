from django.urls import path
from . import views

urlpatterns = [
    path('', views.discussion_home, name='discussion_home'),
    path('new/', views.create_thread, name='create_thread'),
    path('<int:pk>/', views.thread_detail, name='thread_detail'),
    path('<int:pk>/edit/', views.edit_thread, name='edit_thread'),
    path('<int:pk>/delete/', views.delete_thread, name='delete_thread'),
    path('<int:pk>/close/', views.toggle_close, name='toggle_close'),
    path('<int:pk>/pin/', views.toggle_pin, name='toggle_pin'),
    path('reply/<int:pk>/edit/', views.edit_reply, name='edit_reply'),
    path('reply/<int:pk>/delete/', views.delete_reply, name='delete_reply'),
    path('reply/<int:pk>/accept/', views.mark_accepted, name='mark_accepted'),
    path('vote/thread/<int:pk>/up/', views.vote_thread, {'value': 1}, name='vote_thread_up'),
    path('vote/thread/<int:pk>/down/', views.vote_thread, {'value': -1}, name='vote_thread_down'),
    path('vote/reply/<int:pk>/up/', views.vote_reply, {'value': 1}, name='vote_reply_up'),
    path('vote/reply/<int:pk>/down/', views.vote_reply, {'value': -1}, name='vote_reply_down'),
]
