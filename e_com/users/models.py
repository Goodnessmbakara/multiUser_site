from django.db import models

# Create your models here.
class Freelancer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    skillsets = models.TextField(default="programmer")
    # Other fields as needed

class Employer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # Other fields as needed
