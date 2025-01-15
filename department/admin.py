from django.contrib import admin
from .models import *


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    list_per_page = 10

admin.site.register(Department, DepartmentAdmin)
