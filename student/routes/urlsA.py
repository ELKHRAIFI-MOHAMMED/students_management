from django.urls import path
from student.views.viewsA import AssignmentManagementView, AssignmentDeleteView
from django.views.decorators.http import require_http_methods
urlpatterns = [
    path('', AssignmentManagementView.as_view(), name='assignment-management'),
    path('<int:assignment_id>/edit/', AssignmentManagementView.as_view(), name='assignment-edit'),
    path('<int:assignment_id>/delete/', require_http_methods(["GET", "POST"])(AssignmentDeleteView.as_view()), name='assignment-delete'), 
]

# path('', AssignmentListView.as_view(), name='assignment-list'),
    # path('new/', AssignmentCreateView.as_view(), name='assignment-create'),
    # path('<int:pk>/edit/', AssignmentUpdateView.as_view(), name='assignment-update'),
    # path('<int:pk>/delete/', AssignmentDeleteView.as_view(), name='assignment-delete'),