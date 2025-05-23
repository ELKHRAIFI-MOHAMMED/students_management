from django import forms
from .models import Student
from .models import FieldOfStudy
from .models import Class,Assignment
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'gender', 'address', 'class_group']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'class_group': forms.Select(attrs={'class': 'form-select'}),
        }


class FieldOfStudyForm(forms.ModelForm):
    class Meta:
        model = FieldOfStudy
        fields = ['name']

class ClassGroupForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'years', 'field_of_study']

from django import forms
from .models import Module

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'hours']


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['field_of_study', 'module']
        widgets = {
            'field_of_study': forms.Select(attrs={'class': 'form-select'}),
            'module': forms.Select(attrs={'class': 'form-select'}),
        }