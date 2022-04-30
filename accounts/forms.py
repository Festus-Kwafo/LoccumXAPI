from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Professional, Client
    


class ProfessionalSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    gender = forms.ChoiceField(required=True)
    about_me = forms.Textarea()
    service = forms.CharField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_professional = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.phone_number=self.cleaned_data.get('phone_number')
        user.save()
        professional = Professional.objects.create(user=user)
        professional.gender=self.cleaned_data.get('gender')
        professional.about_me=self.cleaned_data.get('about_me')
        professional.service=self.cleaned_data.get('service')
        professional.save()
        return user

class ClientSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    name_organisation = forms.CharField(required=True)
    location = forms.CharField(required=True)
    service = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.phone_number=self.cleaned_data.get('phone_number')
        user.save()
        client = Client.objects.create(user=user)
        client.name_organisation =self.cleaned_data.get('name_organisation')
        client.location=self.cleaned_data.get('location')
        client.service=self.cleaned_data.get('service')
        client.save()
        return user