
from requests import request
from rest_framework import generics, permissions
from .models import *
from .serializers import *
from .permissions import IsInstitutionOrReadOnly, IsLoccumOrReadOnly, IsLoccumUser, IsInstitutionUser
# Create your views here.


class CreateJob(generics.ListCreateAPIView):
    #allow Institution to Create and View jobs 
    permission_classes = (IsInstitutionUser,) 
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.filter(created_by=self.request.user)

class ListJobAll(generics.ListAPIView):
    #allow Loccum all View jobs 
    permission_classes = (IsLoccumUser,) 
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.all()

class DetailJob(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsInstitutionOrReadOnly,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class FulltimeJob(generics.ListAPIView):
    #List Jobs that are fulltime/permanent
    permission_classes = (IsLoccumUser,)
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.filter(job_type="PERMANENT")
class ShiftTImeJob(generics.ListAPIView):
    #List Jobs that are Shift
    permission_classes = (IsLoccumUser,)
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.filter(job_type="SHIFT")