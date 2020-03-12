from django.db import models

# Create your models here.

class AppUser(models.Model):
    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('Customer', 'Customer')
    ]
    name = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 20)
    email = models.EmailField()
    password = models.CharField(max_length = 20)
    role = models.CharField(max_length = 20, choices = ROLE_CHOICES, default = 'Manager')
