from django.db import models
from company.models import Company
from department.models import Department
from egyptian_phone_validator.validators import validate_egyptian_phone_number
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
    first_name = models.CharField(max_length=100,null=False, blank=False)
    last_name = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(max_length=245, unique=True, null=False, blank=False)
    phone = models.CharField(
        max_length=11,
        validators=[validate_egyptian_phone_number],
        help_text="Enter a valid Egyptian phone number (e.g., 01012345678).",
        null=False,
        blank=False
    )
    national_number = models.CharField(max_length=15, unique=True, null=False, blank=False)
    adress = models.TextField(max_length=150, null=False, blank=False)
    position = models.CharField(max_length=100, choices=Position)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    hire_date = models.DateField(auto_now_add=True)
    projects = models.ManyToManyField(Project, related_name='assigned_projects')
    has_account = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name + ' ' + self.last_name)
        super(Employee, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    @property
    def years_with_company(self):
        today = date.today()
        delta = today - self.hire_date
        return delta.days // 365
    
    @property
    def get_project_count(self):
        return self.projects.count()
    
