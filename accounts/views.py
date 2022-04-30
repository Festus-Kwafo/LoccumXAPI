from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from accounts.serializers import ProfessionalCustomRegistrationSerializer, ClientCustomRegistrationSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import *
from .serializers import *
# Create your views here.

class ClientRegistrationView(RegisterView):
    serializer_class = ClientCustomRegistrationSerializer

class ProfessionalRegistrationView(RegisterView):
    serializer_class = ProfessionalCustomRegistrationSerializer


class ClientLoginView(generics.ListAPIView):
    queryset = Professional.objects.all()
    serializer_class = ClientViewSerializer