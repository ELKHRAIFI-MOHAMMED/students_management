from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from student.models import Student,Class,Module,Grade 
from student.forms import StudentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers import serialize
import json

from django.contrib import messages

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

def student_list_by_class(request, pk):  # Accept 'pk' parameter from URL
    # Get the specific class or return 404 if not found
    class_obj = get_object_or_404(Class, pk=pk)
    
    # Get all students in this class
    #students = class_obj.student_set.all().order_by('last_name', 'first_name')
    students =Student.objects.filter(class_group=class_obj.id).order_by('last_name', 'first_name')
    
    context = {
        'class': class_obj,
        'students': students,
    }
    return render(request, 'student/class_students.html', context)

def enter_grades(request, class_id):
    class_obj = get_object_or_404(Class, pk=class_id)
    students = Student.objects.filter(class_group=class_obj).order_by('last_name', 'first_name')
    modules = Module.objects.filter(
        assignment__field_of_study=class_obj.field_of_study
    ).distinct().order_by('name')

    # Préparation des données structurées
    grade_data = {}
    for grade in Grade.objects.filter(student__in=students, module__in=modules):
        key = f"{grade.student_id}_{grade.module_id}"
        grade_data[key] = {
            'grades': grade.grade_list,
            'average': sum(g for g in grade.grade_list if g is not None)/len([g for g in grade.grade_list if g is not None]) 
                      if any(grade.grade_list) else None
        }

    # Structure pour le template
    students_data = []
    for student in students:
        student_modules = []
        for module in modules:
            key = f"{student.id}_{module.id}"
            grades = grade_data.get(key, {}).get('grades', ['', '', '', ''])
            student_modules.append({
                'module_id': module.id,
                'grades': grades,
                'average': grade_data.get(key, {}).get('average')
            })
        students_data.append({
            'student': student,
            'modules': student_modules
        })

    if request.method == 'POST':
        for student in students:
            for module in modules:
                grades = [
                    request.POST.get(f'grade_{student.id}_{module.id}_1'),
                    request.POST.get(f'grade_{student.id}_{module.id}_2'),
                    request.POST.get(f'grade_{student.id}_{module.id}_3'),
                    request.POST.get(f'grade_{student.id}_{module.id}_4'),
                ]
                # Filtrer les valeurs vides
                valid_grades = [float(g) for g in grades if g]
                
                if valid_grades:
                    grade_obj, created = Grade.objects.update_or_create(
                        student=student,
                        module=module,
                        defaults={'grade_list': valid_grades}
                    )
        
        messages.success(request, "Les notes ont été enregistrées avec succès!")
        #return redirect('class-students', pk=class_id)

    return render(request, 'student/enter_grades.html', {
        'class': class_obj,
        'students_data': students_data,
        'modules': modules
    })


def student_grades_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    modules = Module.objects.all()

    modules_with_grades = []

    for module in modules:
        grade_obj = Grade.objects.filter(student=student, module=module).first()
        if grade_obj:
            notes = grade_obj.grade_list[:4]  # Take max 4 grades
            while len(notes) < 4:
                notes.append(None)  # Fill missing grades with None
            # Calculate average (ignore None values)
            valid_notes = [n for n in notes if n is not None]
            moyenne = round(sum(valid_notes)/len(valid_notes), 2) if valid_notes else None
        else:
            notes = [None] * 4
            moyenne = None

        modules_with_grades.append({
            'module': {  # Convert Module to dictionary
                'id': module.id,
                'name': module.name,
                # Add other module fields you need
            },
            'notes': notes,
            'moyenne': moyenne
        })

    moyenne_generale = student.moyenne_generale()

    data = {
        "student": {
            "id": student.id,
            # Add other student fields you need
        },
        "modules": modules_with_grades,
        "overall_average": moyenne_generale,
    }

    #return JsonResponse(data)
    return render(request, 'student/student_grades.html', {
        'student': student,
        'modules_with_grades': modules_with_grades,
        'moyenne_generale': moyenne_generale
    })

