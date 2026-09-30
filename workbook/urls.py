from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.workbook_detail, name='workbook_detail'),
    path('<int:pk>/worksheet/', views.worksheet, name='workbook_worksheet'),
    path('<int:pk>/pupil/<int:user_pk>/', views.review, name='workbook_review'),
    path('item/<int:item_pk>/appeal/', views.appeal, name='workbook_appeal'),
    path('appeals/', views.appeals, name='workbook_appeals'),
]
