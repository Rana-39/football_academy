from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('player', 'Player'),
        ('coach', 'Coach'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='player')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    academy_code = models.CharField(max_length=10, blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
