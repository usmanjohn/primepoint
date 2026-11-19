from django.urls import path
from . import views

# DEMO: get / process / compare need Oracle — they open the 'internal only' page instead.
urlpatterns = [
    path('', views.portfel_home, name = 'portfel-home'),
    path('result/<str:dept_type>/', views.portfel_result, name = 'portfel-result'),
    path('download/', views.download_portfel_summary, name = 'download-portfel-summary'),
]