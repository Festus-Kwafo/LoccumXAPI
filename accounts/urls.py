from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register/locum/', LocumRegistrationView.as_view(), name="locum_register" ),
    path('register/institution/', InstitutionRegistrationView.as_view(), name="institution_register" ),
    path('professionals/', ClientLoginView.as_view(), name='professionals')
]
