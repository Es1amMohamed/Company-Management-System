# Generated by Django 5.1.5 on 2025-01-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_has_account'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(blank=True, null=True, related_name='assigned_projects', to='projects.project'),
        ),
    ]
