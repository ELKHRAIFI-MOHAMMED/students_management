from django.shortcuts import render, redirect, get_object_or_404
from student.models import FieldOfStudy,Class
from student.forms  import ClassGroupForm  # À créer (je te le donne juste après)

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class/class_list.html', {'classes': classes})

def class_create(request):
    if request.method == 'POST':
        form = ClassGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class-list')
    else:
        form = ClassGroupForm()
    return render(request, 'class/class_form.html', {'form': form})

def class_update(request, pk):
    class_group = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        form = ClassGroupForm(request.POST, instance=class_group)
        if form.is_valid():
            form.save()
            return redirect('class-list')
    else:
        form = ClassGroupForm(instance=class_group)
    return render(request, 'class/class_form.html', {'form': form})

def class_delete(request, pk):
    class_group = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        class_group.delete()
        return redirect('class-list')
    return render(request, 'class/class_confirm_delete.html', {'class_group': class_group})

