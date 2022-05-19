from django.db import models
from core.settings import AUTH_USER_MODEL
# Create your models here.
class Job(models.Model):
    JOB_TYPE = (
        ("PERMANENT", "Permanent"),
        ("SHIFT", "Shift")
    )
    created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    name_organization = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    description = models.TextField()
    min_salary = models.FloatField()
    max_salary = models.FloatField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPE, null=True)
    expiry_date = models.DateField(auto_now_add=False)
    

    def __str__(self):
        return self.title

class Cart(models.Model):
    cart_id = models.OneToOneField(AUTH_USER_MODEL,  on_delete=models.CASCADE, primary_key=True,  unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    jobs = models.ManyToManyField(Job)


    class Meta: 
        ordering = ['cart_id', '-created_at',]

    def __str__(self):
        return self.cart_id
    