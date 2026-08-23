from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    # Classroom CRUD
    path('', views.classroom_list, name='list'),
    path('create/', views.classroom_create, name='create'),
    path('<int:pk>/', views.classroom_detail, name='detail'),
    path('<int:pk>/edit/', views.classroom_edit, name='edit'),
    path('<int:pk>/delete/', views.classroom_delete, name='delete'),
    path('<int:pk>/manage/', views.classroom_manage, name='manage'),

    # Lessons
    path('<int:classroom_pk>/lessons/create/', views.lesson_create, name='lesson_create'),
    path('<int:classroom_pk>/lessons/<int:lesson_pk>/', views.lesson_detail, name='lesson_detail'),
    path('<int:classroom_pk>/lessons/<int:lesson_pk>/edit/', views.lesson_edit, name='lesson_edit'),
    path('<int:classroom_pk>/lessons/<int:lesson_pk>/delete/', views.lesson_delete, name='lesson_delete'),
    path('<int:classroom_pk>/lessons/<int:lesson_pk>/assign/', views.lesson_assign_homework, name='lesson_assign'),
    path('<int:classroom_pk>/lessons/<int:lesson_pk>/notes/upload/', views.lesson_note_upload, name='note_upload'),
    path('<int:classroom_pk>/lessons/<int:lesson_pk>/notes/<int:note_pk>/delete/', views.lesson_note_delete, name='note_delete'),

    # Homework
    path('<int:classroom_pk>/homework/', views.homework_list, name='homework_list'),
    path('<int:classroom_pk>/homework/new/', views.homework_create, name='homework_create'),
    path('<int:classroom_pk>/homework/<int:hw_pk>/', views.homework_detail, name='homework_detail'),
    path('<int:classroom_pk>/homework/<int:hw_pk>/edit/', views.homework_edit, name='homework_edit'),
    path('<int:classroom_pk>/homework/<int:hw_pk>/delete/', views.homework_delete, name='homework_delete'),
    path('<int:classroom_pk>/homework/<int:hw_pk>/items/add/', views.homework_add_item, name='homework_add_item'),
    path('<int:classroom_pk>/homework/<int:hw_pk>/items/remove/', views.homework_remove_item, name='homework_remove_item'),
    path('<int:classroom_pk>/homework/<int:hw_pk>/assign/', views.homework_assign, name='homework_assign'),
    path('<int:classroom_pk>/homework/<int:hw_pk>/assignments/<int:assignment_pk>/grade/', views.homework_grade, name='homework_grade'),
    path('<int:classroom_pk>/homework/<int:hw_pk>/assignments/<int:assignment_pk>/remove/', views.homework_unassign, name='homework_unassign'),

    # Students
    path('<int:classroom_pk>/students/', views.students, name='students'),
    path('<int:classroom_pk>/students/add/', views.student_add, name='student_add'),
    path('<int:classroom_pk>/students/register/', views.attendance_register, name='attendance_register'),
    path('<int:classroom_pk>/students/<int:panda_pk>/', views.student_detail, name='student_detail'),
    path('<int:classroom_pk>/students/<int:panda_pk>/remove/', views.student_remove, name='student_remove'),
    path('<int:classroom_pk>/students/<int:panda_pk>/attendance/', views.attendance_mark, name='attendance_mark'),
    path('<int:classroom_pk>/students/<int:panda_pk>/certificate/', views.certificate_issue, name='certificate_issue'),
    path('<int:classroom_pk>/certificates/<int:cert_pk>/delete/', views.certificate_delete, name='certificate_delete'),

    # Groups
    path('<int:classroom_pk>/groups/create/', views.group_create, name='group_create'),
    path('<int:classroom_pk>/groups/<int:group_pk>/edit/', views.group_edit, name='group_edit'),
    path('<int:classroom_pk>/groups/<int:group_pk>/delete/', views.group_delete, name='group_delete'),

    # Payments
    path('<int:classroom_pk>/payments/', views.payments, name='payments'),
    path('<int:classroom_pk>/payments/add/', views.payment_add, name='payment_add'),
    path('<int:classroom_pk>/payments/<int:payment_pk>/paid/', views.payment_mark_paid, name='payment_mark_paid'),
    path('<int:classroom_pk>/payments/<int:payment_pk>/delete/', views.payment_delete, name='payment_delete'),

    # Notes and links
    path('<int:classroom_pk>/resources/', views.resources, name='resources'),
    path('<int:classroom_pk>/resources/add/', views.resource_add, name='resource_add'),
    path('<int:classroom_pk>/resources/<int:res_pk>/delete/', views.resource_delete, name='resource_delete'),

    # Discussion
    path('<int:classroom_pk>/discussion/', views.discussion_list, name='discussion_list'),
    path('<int:classroom_pk>/discussion/create/', views.discussion_create, name='discussion_create'),
    path('<int:classroom_pk>/discussion/<int:thread_pk>/', views.discussion_thread, name='discussion_thread'),
    path('<int:classroom_pk>/discussion/<int:thread_pk>/delete/', views.discussion_delete, name='discussion_delete'),
]
