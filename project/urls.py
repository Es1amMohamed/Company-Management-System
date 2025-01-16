from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('company/', include('company.urls', namespace='company')),
    path('employee/', include('employee.urls', namespace='employee')),
    path('department/', include('department.urls', namespace='department')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
