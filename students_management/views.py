from django.shortcuts import render
from django.db.models import Count
from student.models import Student, Module, FieldOfStudy

def home(request):
    # Get counts for all statistics
    context = {
        'total_students': Student.objects.count(),
        'total_modules': Module.objects.count(),
        'total_fields': FieldOfStudy.objects.count(),
        
        # Additional statistics you might want
        'students_by_field': FieldOfStudy.objects.annotate(
            student_count=Count('class__student')
        ).order_by('-student_count'),
        
        'modules_by_field': FieldOfStudy.objects.annotate(
            module_count=Count('assignment__module')
        ).order_by('-module_count'),
    }
    
    return render(request, 'home.html', context)