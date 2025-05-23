from django.urls import path
from student.views import viewsM

urlpatterns = [
    path('', viewsM.module_list, name='module-list'),
    path('add/', viewsM.module_create, name='module-create'),
    path('edit/<int:pk>/', viewsM.module_update, name='module-update'),
    path('delete/<int:pk>/', viewsM.module_delete, name='module-delete'),
]
