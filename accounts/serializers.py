import imp
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.views import LoginSerializer
from .models import *

class LocumCustomRegistrationSerializer(RegisterSerializer):
    
    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
    )
    locum = serializers.PrimaryKeyRelatedField(read_only=True,)
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True)
    gender = serializers.ChoiceField(required=True, choices=GENDER)
    about_me = serializers.CharField()
    service = serializers.CharField(required=True)
    id_file = serializers.FileField(required=True)
    license_file = serializers.FileField(required=True)
    cv_file = serializers.FileField(required=True)

    def get_cleaned_data(self):
            data = super(LocumCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'name' : self.validated_data.get('name', ''),
                'email': self.validated_data.get('email', ''),
                'phone_number': self.validated_data.get('phone_number', ''),
                'gender': self.validated_data.get('gender', ''),
                'about_me': self.validated_data.get('about_me', ''),
                'service': self.validated_data.get('service', ''),
                'id_file': self.validated_data.get('id_file', ''),
                'license_file': self.validated_data.get('license_file', ''),
                'cv_file': self.validated_data.get('cv_file', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(LocumCustomRegistrationSerializer, self).save(request)
        user.is_locum = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.phone_number=self.cleaned_data.get('phone_number')
        user.save()
        locum = Locum(
            user=user,
            gender=self.cleaned_data.get('gender'),
            about_me=self.cleaned_data.get('about_me'),
            service=self.cleaned_data.get('service'),
            id_file=self.cleaned_data.get('id_file'),
            license_file=self.cleaned_data.get('license_file'),
            cv_file=self.cleaned_data.get('cv_file'),
            )
        locum.save()
        return user


class InstitutionCustomRegistrationSerializer(RegisterSerializer):
    client = serializers.PrimaryKeyRelatedField(read_only=True,)
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True)
    location = serializers.CharField(required=True)
    name_organisation = serializers.CharField()
    service = serializers.CharField(required=True)
    id_file = serializers.FileField(required=True)
    license_file = serializers.FileField(required=True)

    def get_cleaned_data(self):
            data = super(InstitutionCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'name' : self.validated_data.get('name', ''),
                'email': self.validated_data.get('email', ''),
                'phone_number': self.validated_data.get('phone_number', ''),
                'location': self.validated_data.get('location', ''),
                'name_organisation': self.validated_data.get('name_organisation', ''),
                'service': self.validated_data.get('service', ''),
                'id_file': self.validated_data.get('id_file', ''),
                'license_file': self.validated_data.get('license_file', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(InstitutionCustomRegistrationSerializer, self).save(request)
        user.is_institution = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.phone_number=self.cleaned_data.get('phone_number')
        user.save()
        institution = Institution(
            user=user,
            location=self.cleaned_data.get('location'),
            name_organisation=self.cleaned_data.get('name_organisation'),
            service=self.cleaned_data.get('service'),
            id_file=self.cleaned_data.get('id_file'),
            license_file=self.cleaned_data.get('license_file'),
            )
        institution.save()
        return user
class InstitutionCustomRegistrationSerializer(RegisterSerializer):
    client = serializers.PrimaryKeyRelatedField(read_only=True,)
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True)
    location = serializers.CharField(required=True)
    name_organisation = serializers.CharField()
    service = serializers.CharField(required=True)
    id_file = serializers.FileField(required=True)
    license_file = serializers.FileField(required=True)

    def get_cleaned_data(self):
            data = super(InstitutionCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'name' : self.validated_data.get('name', ''),
                'email': self.validated_data.get('email', ''),
                'phone_number': self.validated_data.get('phone_number', ''),
                'location': self.validated_data.get('location', ''),
                'name_organisation': self.validated_data.get('name_organisation', ''),
                'service': self.validated_data.get('service', ''),
                'id_file': self.validated_data.get('id_file', ''),
                'license_file': self.validated_data.get('license_file', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(InstitutionCustomRegistrationSerializer, self).save(request)
        user.is_institution = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.phone_number=self.cleaned_data.get('phone_number')
        user.save()
        institution = Institution(
            user=user,
            location=self.cleaned_data.get('location'),
            name_organisation=self.cleaned_data.get('name_organisation'),
            service=self.cleaned_data.get('service'),
            id_file=self.cleaned_data.get('id_file'),
            license_file=self.cleaned_data.get('license_file'),
            )
        institution.save()
        return user


class ClientViewSerializer(serializers.ModelSerializer):
    my_client_data = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= Locum
        fields = ('my_client_data', 'gender', 'about_me', 'service',)
    def get_my_client_data(self, obj):
        return {
            "name":obj.user.username
        }

