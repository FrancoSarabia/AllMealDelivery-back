from rest_framework import serializers
from ..models.dish_type import DishType

class DishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishType
        fields = ['_id', 'name']