from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
