from django.db import models
from django.contrib.auth.models import User, auth


# Create your models here.

class Passwords(models.Model):
    user = models.CharField(max_length=25)
    site_name = models.CharField(max_length=100)
    site_url = models.URLField(max_length=100)
    # sitehttp = models.URLField(max_length = 100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    phoneNo = models.CharField(max_length=15)

class Documents(models.Model):
    
    user = models.CharField(max_length=25)
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
