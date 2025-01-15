from django.contrib import admin
from .models import *

class companyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name', 'location']

admin.site.register(Company, companyAdmin)
