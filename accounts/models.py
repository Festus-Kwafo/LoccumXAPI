from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField



class User(AbstractUser):
    is_professional =models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.EmailField()

class Professional(models.Model):

    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=20, null=True, choices=GENDER)
    about_me = models.TextField()
    service = models.CharField(max_length=255, null=True)
    id_file = models.FileField(null=True)
    license_file = models.FileField(null=True)
    cv_file = models.FileField(null=True)

    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=255, null=True)
    name_organisation = models.CharField(max_length=255, null=True)
    service = models.CharField(max_length=255, null=True)
    id_file = models.FileField(null=True)
    license_file = models.FileField(null=True)


