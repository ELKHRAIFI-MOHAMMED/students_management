from django.urls import path
from student.views import viewsC

urlpatterns = [
    path('', viewsC.class_list, name='class-list'),
    path('add/', viewsC.class_create, name='class-create'),
    path('edit/<int:pk>/', viewsC.class_update, name='class-update'),
    path('delete/<int:pk>/', viewsC.class_delete, name='class-delete'),
]
