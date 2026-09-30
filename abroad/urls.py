from django.urls import path

from . import views

urlpatterns = [
    path('', views.abroad_home, name='abroad_home'),
    path('guides/<slug:slug>/', views.guide_detail, name='abroad_guide'),
    path('scholarships/', views.scholarship_list, name='abroad_scholarships'),
    path('scholarships/<slug:slug>/', views.scholarship_detail, name='abroad_scholarship'),
    path('samples/<slug:slug>/', views.sample_detail, name='abroad_sample'),
    path('samples/<slug:slug>/planner/', views.sample_planner, name='abroad_planner'),
    path('universities/', views.university_list, name='abroad_universities'),
    path('checklist/', views.checklist, name='abroad_checklist'),
]
