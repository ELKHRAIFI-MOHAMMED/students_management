# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from student.models import Assignment
# from student.forms import AssignmentForm

# class AssignmentListView(ListView):
#     model = Assignment
#     template_name = 'assignments/assignment_list.html'
#     context_object_name = 'assignments'

# class AssignmentCreateView(CreateView):
#     model = Assignment
#     form_class = AssignmentForm
#     template_name = 'assignments/assignment_form.html'
#     success_url = reverse_lazy('assignment-list')

# class AssignmentUpdateView(UpdateView):
#     model = Assignment
#     form_class = AssignmentForm
#     template_name = 'assignments/assignment_form.html'
#     success_url = reverse_lazy('assignment-list')

# class AssignmentDeleteView(DeleteView):
#     model = Assignment
#     template_name = 'assignments/assignment_confirm_delete.html'
#     success_url = reverse_lazy('assignment-list')
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from student.models import Assignment, FieldOfStudy, Module

class AssignmentManagementView(View):
    template_name = 'assignments/assignment_management.html'
    
    def get(self, request, *args, **kwargs):
        assignment_id = kwargs.get('assignment_id')
        assignment = None
        if assignment_id:
            assignment = get_object_or_404(Assignment, id=assignment_id)
        
        context = {
            'assignments': Assignment.objects.all().select_related('field_of_study', 'module'),
            'field_of_studies': FieldOfStudy.objects.all(),
            'modules': Module.objects.all(),
            'assignment': assignment,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        assignment_id = kwargs.get('assignment_id')
        field_of_study_id = request.POST.get('field_of_study')
        module_id = request.POST.get('module')
        
        if not field_of_study_id or not module_id:
            messages.error(request, "Both Field of Study and Module are required")
            return redirect('assignment-management')
        
        try:
            field_of_study = FieldOfStudy.objects.get(id=field_of_study_id)
            module = Module.objects.get(id=module_id)
            
            if assignment_id:
                assignment = get_object_or_404(Assignment, id=assignment_id)
                assignment.field_of_study = field_of_study
                assignment.module = module
                assignment.save()
                messages.success(request, "Assignment updated successfully")
            else:
                if Assignment.objects.filter(field_of_study=field_of_study, module=module).exists():
                    messages.warning(request, "This assignment already exists")
                else:
                    Assignment.objects.create(field_of_study=field_of_study, module=module)
                    messages.success(request, "Assignment created successfully")
            
            return redirect('assignment-management')
        
        except (FieldOfStudy.DoesNotExist, Module.DoesNotExist):
            messages.error(request, "Invalid selection")
            return redirect('assignment-management')

class AssignmentDeleteView(View):
    def post(self, request, assignment_id):
        assignment = get_object_or_404(Assignment, id=assignment_id)
        assignment.delete()
        messages.success(request, "Assignment deleted successfully")
        return redirect('assignment-management')