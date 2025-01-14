from django.db import models
from company.models import Company
import uuid
from django.utils.text import slugify

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, related_name='departments' ,on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    @property
    def get_employee_count(self):
        return self.employees.count()
    
    @property
    def get_project_count(self):
        return self.projects.count()
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
