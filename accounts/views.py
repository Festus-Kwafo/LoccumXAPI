from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from .serializers import LocumCustomRegistrationSerializer, InstitutionCustomRegistrationSerializer, ClientViewSerializer
from rest_framework import generics
from .permissions import IsUserOrReadOnly
from .models import *

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

class UserLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "some message", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response



