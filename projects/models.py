from django.db import models
import uuid
from django.utils.text import slugify
from company.models import Company
from department.models import Department

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_projects')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_projects')
    employees = models.ManyToManyField('employee.Employee', related_name='participated_projects')
    start_date = models.DateField()
    end_date = models.DateField()
    slug = models.SlugField(null=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    @property
    def project_duration(self):
        return self.end_date - self.start_date