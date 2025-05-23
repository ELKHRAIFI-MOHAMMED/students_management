from django.urls import path
from student.views import views

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student-list'),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('new/', views.StudentCreateView.as_view(), name='student-create'),
    path('<int:pk>/update/', views.StudentUpdateView.as_view(), name='student-update'),
    path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),
    path('<int:pk>/studentsClass/', views.student_list_by_class, name='class-students'),
    path('<int:class_id>/enter-grades/', views.enter_grades, name='enter-grades'),
    path('<int:pk>/grades/', views.student_grades_view, name='student-grades'),
]
