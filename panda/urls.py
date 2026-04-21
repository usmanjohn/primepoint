from django.urls import path
from . import views

urlpatterns = [
    path('', views.panda_home, name='panda-home'),
 ]