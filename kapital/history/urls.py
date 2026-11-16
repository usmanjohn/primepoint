from django.urls import path
from . import views

# If your project already has these routes, just make sure the NAMES match:
#   'history'          -> the history page (cleanup redirects back here)
#   'datasets-files'   -> NEW: admin page with every file in datasets/
urlpatterns = [
    path('', views.home, name='history'),
    path('download/<str:filename>/', views.download_file, name='download-file'),
    path('export-summary/', views.export_model_to_excel, name='export-model-to-excel'),
    path('cleanup/', views.cleanup_old_portfels, name='cleanup-portfels'),
    path('datasets/', views.datasets_files, name='datasets-files'),
]
