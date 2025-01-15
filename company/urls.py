from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter


app_name = 'company'

router = DefaultRouter()
router.register('', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]