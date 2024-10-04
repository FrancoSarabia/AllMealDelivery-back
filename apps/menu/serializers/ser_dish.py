from rest_framework import serializers
from ..models.dish import Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['_id', 'name', 'description', 'price', 'image']