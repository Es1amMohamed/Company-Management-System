from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *



class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer