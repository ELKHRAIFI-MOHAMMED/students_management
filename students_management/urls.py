from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    
    # Students app routes
    path('students/', include('student.routes.urls'), name='students-home'),
    
    # Fields of study routes
    path('fields/', include('student.routes.urlsF'), name='fields-home'),
       path('class/', include('student.routes.urlsC'), name='class-home'),
        path('module/', include('student.routes.urlsM'), name='module-home'),
        path('assignment/', include('student.routes.urlsA'), name='assignments-home'),
    
    # Home page
    path('', views.home, name='home'),
    
    # Add authentication URLs (optional)
    # path('accounts/', include('django.contrib.auth.urls')),
]