from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='people/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='people/logout.html'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='people/password_change.html',
        success_url=reverse_lazy('password_change_done'),
    ), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='people/password_change_done.html',
    ), name='password_change_done'),
]
