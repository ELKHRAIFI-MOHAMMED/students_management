from django.db import models
from django.urls import reverse

class FieldOfStudy(models.Model):  # Renamed 'Filier' to 'FieldOfStudy'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Class(models.Model):  # Renamed 'Class' to 'ClassGroup'
    name = models.CharField(max_length=100)
    years = models.IntegerField()  # Duration in years
    field_of_study = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=100)
    hours = models.IntegerField()  # Number of hours

    def __str__(self):
        return self.name

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField(blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})
    
    def moyenne_generale(self):
        # Assuming Grade model has a related_name 'grades' to refer to grades from the student
        grades = self.grade_set.all()  # Use 'grade_set' to access related Grade objects
        if grades.exists():
            return round(sum(grade.grade_list[0] for grade in grades) / grades.count(), 2)  # Assuming grade_list is a list and we are taking the first grade as the score
        return 0

class Assignment(models.Model):  # Renamed 'Affectation' to 'Assignment'
    field_of_study = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return f"Assignment of {self.module} in {self.field_of_study}"


class Grade(models.Model):  # Renamed 'Note' to 'Grade'
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # ForeignKey to Student model
    grade_list = models.JSONField()  # JSON to store the list of grades

    def __str__(self):
        return f"Grades for {self.student.first_name} {self.student.last_name} in {self.module.name}"
