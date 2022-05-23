from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

class User(AbstractUser):
    is_locum =models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=20, null=True)

    email = models.EmailField()

    def __str__(self):
        return self.username
    
    

class Locum(models.Model):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/%Y/%m/%d/', null=True)
    gender = models.CharField(max_length=20, null=True, choices=GENDER)
    about_me = models.TextField()
    service = models.CharField(max_length=255, null=True)
    id_file = models.FileField(upload_to='validation/%Y/%m/%d/', null=True)
    license_file = models.FileField(upload_to='validation/%Y/%m/%d/', null=True)
    cv_file = models.FileField(upload_to='validation/%Y/%m/%d/', null=True)

    def __str__(self):
        return self.user.username

    
class Institution(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=255, null=True)
    name_organisation = models.CharField(max_length=255, null=True)
    service = models.CharField(max_length=255, null=True)
    id_file = models.FileField(upload_to='validation/%Y/%m/%d/', null=True)
    license_file = models.FileField(upload_to='validation/%Y/%m/%d/', null=True)


    def __str__(self):
        return self.user.username
        
        