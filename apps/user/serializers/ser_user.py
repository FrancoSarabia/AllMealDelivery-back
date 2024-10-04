from rest_framework import serializers
from ..models.user import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'email', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user
    
    class Meta:
        model = get_user_model()
        fields = "__all__"