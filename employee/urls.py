from django.urls import include, path
from . import views
from rest_framework import routers



app_name = 'employee'

router = routers.DefaultRouter()

router.register('', views.EmployeeView)

urlpatterns = [
    path('', include(router.urls)),
]