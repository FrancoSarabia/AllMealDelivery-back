from rest_framework import serializers
from ..models.profile import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['_id', 'name']