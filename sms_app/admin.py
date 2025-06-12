from django.contrib import admin
from .models import Student, Subject, Enrollment, Grade

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'email')
    search_fields = ('student_id', 'first_name', 'last_name')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'enrollment_date')
    list_filter = ('subject', 'enrollment_date')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'grade_type', 'score', 'max_score', 'percentage')
    list_filter = ('grade_type', 'date_given')
    
    def percentage(self, obj):
        return f"{obj.percentage():.1f}%"