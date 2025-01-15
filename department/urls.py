from django.urls import include, path
from .views import *
from rest_framework import routers





app_name = 'department'

router = routers.DefaultRouter()
router.register('', DepartmentView)

urlpatterns = [
    path('', include(router.urls)),
]