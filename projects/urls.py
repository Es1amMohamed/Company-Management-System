from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'projects'

router = DefaultRouter()
router.register('', ProjectView)

urlpatterns = [
    path('', include(router.urls)),
]