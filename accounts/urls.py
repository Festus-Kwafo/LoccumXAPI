from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register/locum/', LocumRegistrationView.as_view(), name="locum_register" ),
    path('register/institution/', InstitutionRegistrationView.as_view(), name="institution_register" ),
    path('login/institution/', UserLoginView.as_view(), name="institution_login" ),
    path('login/locum/', UserLoginView.as_view(), name="locum_login" ),
    path('locum/', LocumList.as_view(), name='locum'),
    path('locum/<int:pk>', LocumDetail.as_view(), name='professionals_details')
]
