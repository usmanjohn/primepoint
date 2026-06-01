from django.urls import path
from . import views

urlpatterns = [
    path('', views.master_list, name='masters-home'),
    path('create/', views.master_create, name='masters-create'),
    path('certificate/', views.certificate_generator, name='masters-certificate'),
    path('<int:master_id>/', views.master_detail, name='masters-detail'),
    path('update/<int:pk>/', views.master_update, name='update-master'),
    path('delete/<int:pk>/', views.master_delete, name='delete-master'),
    path('<int:pk>/remove-student/<int:panda_pk>/', views.master_remove_student, name='master-remove-student'),

    # My Students management
    path('<int:pk>/my-students/', views.my_students, name='masters-my-students'),
    path('<int:pk>/my-students/add/', views.add_student, name='masters-add-student'),
    path('<int:pk>/my-students/<int:panda_pk>/', views.student_detail, name='masters-student-detail'),
    path('<int:pk>/my-students/<int:panda_pk>/attendance/', views.mark_attendance, name='masters-mark-attendance'),
    path('<int:pk>/my-students/<int:panda_pk>/payment/', views.add_payment, name='masters-add-payment'),
    path('<int:pk>/my-students/<int:panda_pk>/certificate/', views.issue_certificate, name='masters-issue-certificate'),
    path('<int:pk>/payments/<int:payment_pk>/delete/', views.delete_payment, name='masters-delete-payment'),
    path('<int:pk>/certificates/<int:cert_pk>/delete/', views.delete_certificate, name='masters-delete-certificate'),

    # Student certificate view (read-only + download)
    path('certificates/<int:cert_pk>/view/', views.certificate_view, name='certificate-view'),
]
