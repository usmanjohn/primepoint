from django.urls import path

from . import views

urlpatterns = [
    path('', views.balans_home, name='balans-home'),
    path('get', views.balans_get, name='balans-get'),
    path('result', views.balans_result, name='balans-result'),
]
