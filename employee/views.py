from django.contrib import messages
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

@api_view(['POST'])
def user_login(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Request processed successfully"})
        else:
           return Response({"message": "Invalid credentials"})
        

@api_view(['POST'])
@login_required
def change_password(request):
    current_password = request.POST.get('current_password')
    new_password = request.POST.get('new_password')
    user = request.user
    if user.check_password(current_password):
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password changed successfully"})
    else:
        return Response({"message": "Current password is incorrect"})

