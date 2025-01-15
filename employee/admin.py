from django.contrib import admin
from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('first_name', 'last_name', 'email', 'phone',)
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    ordering = ('first_name', 'last_name')

admin.site.register(Employee, EmployeeAdmin)