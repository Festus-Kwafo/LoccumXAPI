from django.urls import path
from .views import ClientRegistrationView, ProfessionalRegistrationView, ClientLoginView

app_name = 'accounts'

urlpatterns = [
    path('register/professional/', ProfessionalRegistrationView.as_view(), name="professional_register" ),
    path('register/client/', ClientRegistrationView.as_view(), name="client_register" ),
    path('professionals/', ClientLoginView.as_view(), name='professionals')
]
