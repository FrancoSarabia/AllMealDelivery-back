from rest_framework import serializers
from ..models.person import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['_id', 'rut', 'name', 'last_name', 'address', 'phone'] 