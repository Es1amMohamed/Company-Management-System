from django.db import models
import uuid
from django.utils.text import slugify

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    slug = models.SlugField(null=True, blank=True)


    @property
    def get_department_count(self):
        return self.departments.count()
    
    @property
    def get_employee_count(self):
        return self.employees.count()
    
    @property
    def get_project_count(self):
        return self.projects.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
