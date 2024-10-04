from rest_framework import serializers

from ..models.dish import Dish
from ..models.menu_dish import MenuDish
from ..serializers.ser_dish import DishSerializer

class MenuDishSerializer(serializers.ModelSerializer):
    dish = DishSerializer(read_only=True)  # Para leer los detalles completos del plato
    dish_id = serializers.PrimaryKeyRelatedField(queryset=Dish.objects.all(), write_only=True, source='dish')

    class Meta:
        model = MenuDish
        fields = ['_id', 'dish', 'dish_id'] # dish_id para crear, dish para leer