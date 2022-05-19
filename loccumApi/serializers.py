from rest_framework import serializers
from .models import Cart, Job

class JobSerializer(serializers.ModelSerializer):
    # created_by = serializers.ReadOnlyField(source='created_by.id', read_only=False)
    class Meta:
        model = Job
        fields = ('created_by','title', 'name_organization', 'location', 'min_salary', 'max_salary', 'expiry_date', 'job_type')


class CartSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(read_only=True, many=True)
    class Meta: 
        model = Cart
        fields = ('cart_id', 'created_at', 'jobs')