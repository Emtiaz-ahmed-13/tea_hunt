from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Extend the User model for profile management
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
