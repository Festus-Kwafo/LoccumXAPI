from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from accounts.serializers import LocumCustomRegistrationSerializer, InstitutionCustomRegistrationSerializer
from rest_framework import generics
from .permissions import IsUserOrReadOnly
from .models import *
from .serializers import *
# Create your views here.

class InstitutionRegistrationView(RegisterView):
    serializer_class = InstitutionCustomRegistrationSerializer

class LocumRegistrationView(RegisterView):
    serializer_class = LocumCustomRegistrationSerializer


class ClientList(generics.ListAPIView):
    queryset = Locum.objects.all()
    serializer_class = ClientViewSerializer
    
class ClientDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsUserOrReadOnly,)
    queryset = Locum.objects.all()
    serializer_class = ClientViewSerializer



