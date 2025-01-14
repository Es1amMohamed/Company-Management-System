from django.db import models
from company.models import Company
from department.models import Department
from projects.models import Project
import uuid
from django.utils.text import slugify
from datetime import date



class Employee(models.Model):

    Position = [
        ('CEO', 'CEO'),
        ('Admin', 'Admin'),
        ('Department Head', 'Department Head'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, required=True)
    email = models.EmailField(max_length=245, unique=True)
    phone = models.CharField(max_length=15, unique=True, required=True)
    national_number = models.CharField(max_length=15, unique=True, required=True)
    adress = models.TextField(max_length=150, required=True)
    position = models.CharField(max_length=100, choices=Position)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    hire_date = models.DateField(auto_now_add=True)
    projects = models.ManyToManyField(Project, related_name='employees')
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Employee, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name 
    
    @property
    def years_with_company(self):
        today = date.today()
        delta = today - self.hire_date
        return delta.days // 365
    
    @property
    def get_project_count(self):
        return self.projects.count()
    
