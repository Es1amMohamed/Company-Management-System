from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date')

admin.site.register(Project, ProjectAdmin)
