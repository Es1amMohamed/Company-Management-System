from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('company/', include('company.urls', namespace='company')),
    path('employee/', include('employee.urls', namespace='employee')),
    path('department/', include('department.urls', namespace='department')),
    path('projects/', include('projects.urls', namespace='projects')),
]
