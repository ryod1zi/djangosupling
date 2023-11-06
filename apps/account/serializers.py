from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'password_confirm', 'profile', 'first_name', 'last_name']

def validate(self, attrs):
    password_confirmation = attrs.pop('password_confirmation')  
