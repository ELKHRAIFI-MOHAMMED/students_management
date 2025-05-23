from django.urls import path
from student.views import viewsF

urlpatterns = [
    path('', viewsF.field_list, name='field_list'),
    path('create/', viewsF.field_create, name='field_create'),
    path('<int:pk>/update/', viewsF.field_update, name='field_update'),
    path('<int:pk>/delete/', viewsF.field_delete, name='field_delete'),
    path('fields/<int:pk>/classes/', viewsF.classes_by_field, name='classes-by-field'),
    
]
