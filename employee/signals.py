from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Employee

@receiver(post_save, sender=Employee)
def create_user_account(sender, instance, created, **kwargs):
    if created:  
        if not instance.has_account:
            user = User.objects.create_user(
                username=instance.email, 
                password='default_password',    
            )    
            instance.has_account = True
            instance.user = user
            instance.save()
