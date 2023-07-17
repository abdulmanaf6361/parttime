from django.db import models
from djongo import models
# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=50)
    college=models.CharField(max_length=100)
    current_location=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=50)
    city=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    
class Recruiter(models.Model):
    name=models.CharField(max_length=50)
    organization=models.CharField(max_length=100)
    current_location=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=50)
    city=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
