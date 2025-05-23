from django.contrib import admin
from .models import FieldOfStudy, Class, Module, Student, Assignment, Grade

# Enregistrement des modèles dans l'interface d'administration

class FieldOfStudyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'years', 'field_of_study')
    list_filter = ('field_of_study',)
    search_fields = ('name',)

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'hours')
    search_fields = ('name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'class_group')
    list_filter = ('class_group',)
    search_fields = ('first_name', 'last_name', 'email')

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('field_of_study', 'module')
    list_filter = ('field_of_study',)
    search_fields = ('field_of_study__name', 'module__name')

class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'module', 'grade_list')
    list_filter = ('module',)
    search_fields = ('student__first_name', 'student__last_name', 'module__name')

# Enregistrer les modèles dans l'admin
admin.site.register(FieldOfStudy, FieldOfStudyAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Grade, GradeAdmin)
