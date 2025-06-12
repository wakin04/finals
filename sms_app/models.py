from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('student', 'subject')
    
    def __str__(self):
        return f"{self.student} enrolled in {self.subject}"

class Grade(models.Model):
    GRADE_TYPES = [
        ('ACT', 'Activity'),
        ('QUIZ', 'Quiz'),
        ('EXAM', 'Exam'),
    ]
    
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    grade_type = models.CharField(max_length=4, choices=GRADE_TYPES)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    max_score = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    date_given = models.DateField()
    comments = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.enrollment.student} - {self.grade_type}: {self.score}/{self.max_score}"
    
    def percentage(self):
        return (self.score / self.max_score) * 100