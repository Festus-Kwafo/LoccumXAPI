from django.urls import path
from .views import *

app_name= 'loccumApi'

urlpatterns = [
    path('job/', AllJob.as_view(), name='all_job'), #list all jobs in the database
    path('job/create', CreateJob.as_view(), name='create_job' ), #List and create jobs according to Institution users
    path('job/all', ListJobAll.as_view(), name='list_job_loccum' ), #List all jobs to loccum users
    path('job/<int:pk>', DetailJob.as_view(), name='job_detail' ), #Detail view of jobs to 
    path('job/fulltime', FulltimeJob.as_view(), name='fulltime_job') #Fulltime jobs 
]
