from django.urls import path
from .views import *

app_name= 'loccumApi'

urlpatterns = [
    path('job/', CreateJob.as_view(), name='job' ), #List and create jobs according to Institution users
    path('job/all', ListJobAll.as_view(), name='job' ), #List all jobs to loccum users
    path('job/<int:pk>', DetailJob.as_view(), name='job' ), #Detail view of jobs to 
]
