from rest_framework import serializers
from .models import User, UserManager, Report

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, 
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'phn']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    # validating password and confirm password while registration
    def validate(self, attrs):
        return attrs
    
    
class UserLoginSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'phn', 'is_active', 'is_admin']


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class LocationSerializer(serializers.Serializer):
    latitude = serializers.CharField(max_length=50)
    longitude = serializers.CharField(max_length=50)