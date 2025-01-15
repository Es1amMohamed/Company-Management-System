from django.shortcuts import render
from .serializers import CompanySerializer
from .models import Company
from rest_framework import viewsets


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
