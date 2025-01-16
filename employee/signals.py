from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
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

            group_name = instance.position  
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
        
        else:
                raise ValueError("A user with this email already exists.")
        

@receiver(post_delete, sender=Employee)
def delete_user_account(sender, instance, **kwargs):
    """
    Signal to delete the User associated with an Employee when the Employee is deleted.
    """
    if instance.user:
        instance.user.delete()
