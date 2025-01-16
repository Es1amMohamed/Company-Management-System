from django.urls import include, path
from . import views
from rest_framework import routers



app_name = 'employee'

router = routers.DefaultRouter()

router.register('', views.EmployeeView)

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('rest_password/', views.change_password, name='rest_password'),
    path('', include(router.urls)),

]