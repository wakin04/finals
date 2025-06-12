from django.urls import path
from . import views
from .views import home  

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),  # Create URL
    path('students/<str:student_id>/', views.student_detail, name='student_detail'),
    path('students/<str:student_id>/update/', views.student_update, name='student_update'),
    path('students/<str:student_id>/delete/', views.student_delete, name='student_delete'),
    
    # Grade URLs
    path('enrollments/<int:enrollment_id>/grades/', views.grade_list, name='grade_list'),
    path('grades/<int:grade_id>/', views.grade_detail, name='grade_detail'),
    path('enrollments/<int:enrollment_id>/grades/create/', views.grade_create, name='grade_create'),
    path('grades/<int:grade_id>/update/', views.grade_update, name='grade_update'),
    path('grades/<int:grade_id>/delete/', views.grade_delete, name='grade_delete'),
 # Enrollment URLs
    path('students/<str:student_id>/enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/create/', views.enrollment_create, name='enrollment_create'),
    path('enrollments/create/<str:student_id>/', views.enrollment_create, name='enrollment_create_for_student'),
    path('enrollments/<int:enrollment_id>/delete/', views.enrollment_delete, name='enrollment_delete'),

]