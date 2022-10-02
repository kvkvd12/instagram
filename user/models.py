from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class UserModel(AbstractUser):
    class Meta:
        db_table = 'user'
    
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True, unique=True)
    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')
    