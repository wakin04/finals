from django.shortcuts import get_object_or_404
from .models import Student, Subject, Enrollment, Grade
from .forms import StudentForm, SubjectForm, EnrollmentForm, GradeForm
from django.shortcuts import render
from .models import Student, Subject

from django.shortcuts import redirect
from .forms import StudentForm
from .models import Student

from django.contrib import messages
from .models import Enrollment, Student, Subject
from .forms import EnrollmentForm


# Student Views
def student_list(request):
    students = Student.objects.all().order_by('last_name')
    return render(request, 'students/list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    enrollments = Enrollment.objects.filter(student=student).select_related('subject')
    return render(request, 'students/detail.html', {
        'student': student,
        'enrollments': enrollments
    })

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form, 'action': 'Create'})

def student_update(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student.student_id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/form.html', {'form': form, 'action': 'Update'})

def student_delete(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/delete.html', {'student': student})

# Grade Views
def grade_list(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    grades = Grade.objects.filter(enrollment=enrollment)
    return render(request, 'grades/list.html', {
        'enrollment': enrollment,
        'grades': grades
    })

def grade_detail(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    return render(request, 'grades/detail.html', {'grade': grade})

def grade_create(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.enrollment = enrollment
            grade.save()
            return redirect('grade_list', enrollment_id=enrollment.id)
    else:
        form = GradeForm()
    return render(request, 'grades/form.html', {
        'form': form,
        'action': 'Create',
        'enrollment': enrollment
    })

def grade_update(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_list', enrollment_id=grade.enrollment.id)
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grades/form.html', {
        'form': form,
        'action': 'Update',
        'enrollment': grade.enrollment
    })

def grade_delete(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    enrollment_id = grade.enrollment.id
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list', enrollment_id=enrollment_id)
    return render(request, 'grades/delete.html', {'grade': grade})



def home(request):
    return render(request, 'home.html', {
        'total_students': Student.objects.count(),
        'total_subjects': Subject.objects.count()
    })



def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to student list after creation
    else:
        form = StudentForm()
    
    return render(request, 'students/form.html', {
        'form': form,
        'action': 'Create Student'  # For template header
    })   


def enrollment_create(request, student_id=None):
    student = None
    if student_id:
        student = get_object_or_404(Student, student_id=student_id)
    
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            if student:
                enrollment.student = student
            enrollment.save()
            messages.success(request, f'Successfully enrolled {enrollment.student} in {enrollment.subject}')
            return redirect('student_detail', student_id=enrollment.student.student_id)
    else:
        initial = {'student': student} if student else {}
        form = EnrollmentForm(initial=initial)
    
    return render(request, 'enrollments/form.html', {
        'form': form,
        'student': student,
        'action': 'Create Enrollment'
    })

def enrollment_list(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    enrollments = Enrollment.objects.filter(student=student).select_related('subject')
    return render(request, 'enrollments/list.html', {
        'student': student,
        'enrollments': enrollments
    })

def enrollment_delete(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    student_id = enrollment.student.student_id
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, f'Successfully removed enrollment for {enrollment.student}')
        return redirect('student_detail', student_id=student_id)
    return render(request, 'enrollments/delete.html', {'enrollment': enrollment})