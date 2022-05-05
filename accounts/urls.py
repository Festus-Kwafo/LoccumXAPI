from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register/locum/', LocumRegistrationView.as_view(), name="locum_register" ),
    path('register/institution/', InstitutionRegistrationView.as_view(), name="institution_register" ),
    path('professionals/', ClientList.as_view(), name='professionals'),
    path('professionals/<int:pk>', ClientDetail.as_view(), name='professionals_details')
]
