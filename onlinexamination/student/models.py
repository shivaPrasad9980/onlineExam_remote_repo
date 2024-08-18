from django.db import models

# Create your models here.
class Student(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Contact = models.IntegerField()
    Address = models.CharField(max_length=50)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    ProfilePicture = models.FileField(upload_to="images", max_length=100)