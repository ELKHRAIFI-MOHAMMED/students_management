from django.shortcuts import render, get_object_or_404, redirect
from student.models import FieldOfStudy,Class
from django.urls import reverse

# List all Fields
def field_list(request):
    fields = FieldOfStudy.objects.all()
    return render(request, 'fields/field_list.html', {'fields': fields})

# Create a new Field
def field_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        FieldOfStudy.objects.create(name=name)
        return redirect('field_list')
    return render(request, 'fields/field_form.html')

# Update a Field
def field_update(request, pk):
    field = get_object_or_404(FieldOfStudy, pk=pk)
    if request.method == 'POST':
        field.name = request.POST.get('name')
        field.save()
        return redirect('field_list')
    return render(request, 'fields/field_form.html', {'field': field})

# Delete a Field
def field_delete(request, pk):
    
    field = get_object_or_404(FieldOfStudy, pk=pk)
    if request.method == 'POST':
        field.delete()
        return redirect('field_list')
    return render(request, 'fields/field_confirm_delete.html', {'field': field})


def classes_by_field(request, pk):
    # Get the field of study or return 404 if not found
    field = get_object_or_404(FieldOfStudy, pk=pk)
    
    # Get all classes for this field
    # classes = Class.objects.filter(field_of_study=field.id).order_by('name')
    classes = field.class_set.all().order_by('name')
    context = {
        'field': field,
        'classes': classes,
    }
    return render(request, 'fields/classes_by_field.html', context)