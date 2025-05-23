from django.shortcuts import render, get_object_or_404, redirect
from student.models import Module
from student.forms import ModuleForm

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'module/module_list.html', {'modules': modules})

def module_create(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('module-list')
    else:
        form = ModuleForm()
    return render(request, 'module/module_form.html', {'form': form})

def module_update(request, pk):
    module = get_object_or_404(Module, pk=pk)
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            return redirect('module-list')
    else:
        form = ModuleForm(instance=module)
    return render(request, 'module/module_form.html', {'form': form})

def module_delete(request, pk):
    module = get_object_or_404(Module, pk=pk)
    if request.method == 'POST':
        module.delete()
        return redirect('module-list')
    return render(request, 'module/module_confirm_delete.html', {'module': module})
