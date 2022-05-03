from statistics import mode
from django.db import models
from core.settings import AUTH_USER_MODEL
# Create your models here.
class Job(models.Model):
    JOB_TYPE = (
        ("PERMANENT", "Permanent"),
        ("SHIFT", "Shift")
    )
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    description = models.TextField()
    salary = models.FloatField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPE, null=True)
    expiry_date = models.DateField()
    