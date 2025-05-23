from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm
from django.shortcuts import render, redirect, get_object_or_404


class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'
    ordering = ['last_name', 'first_name']

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_formulaire.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_formulaire.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
