from django.db import models

# Create your models here.

class Passwords(models.Model):
    site_name = models.CharField(max_length=100)
    site_url = models.URLField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    phoneNo = models.CharField(max_length=15)