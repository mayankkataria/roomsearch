from django.db import models

# Create your models here.

class AppUser(models.Model):
    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('Customer', 'Customer'),
    ] # key should be same as option's plain text in html file
    name = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 20)
    email = models.EmailField()
    password = models.CharField(max_length = 20)
    role = models.CharField(max_length = 20, choices = ROLE_CHOICES, default = 'manager')

    def __str__(self):
        return self.name
