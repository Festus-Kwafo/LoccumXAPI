from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    organisation_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Job
        fields = ('title', 'name_organisation', 'Location', 'salary')
    def get_organisation_name(self, obj):
        return {
            "name":obj.user.name_organisation
        }