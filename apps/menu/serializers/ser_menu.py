from rest_framework import serializers

from ..models.menu import Menu
from ..models.menu_dish import MenuDish
from ..serializers.ser_menu_dish import MenuDishSerializer
from ..serializers.ser_dish import DishSerializer


class MenuSerializer(serializers.ModelSerializer):
    menu_dishes = MenuDishSerializer(many=True, write_only=True)  # Usado para crear platos en el menú
    dishes = MenuDishSerializer(source='menudish_set', many=True, read_only=True)  # Usado para leer los platos en el menú

    class Meta:
        model = Menu
        fields = ['_id', 'name', 'description', 'menu_dishes', 'dishes']

    def create(self, validated_data):
        menu_dishes_data = validated_data.pop('menu_dishes')
        menu = Menu.objects.create(**validated_data)

        # Crear las relaciones en la tabla intermedia MenuDish
        for dish_data in menu_dishes_data:
            MenuDish.objects.create(menu=menu, **dish_data)

        return menu

    def update(self, instance, validated_data):
        # Actualizar el menú
        menu_dishes_data = validated_data.pop('menu_dishes', [])
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Actualizar los platos del menú (borramos los anteriores y agregamos los nuevos)
        instance.menu_dishes.all().delete()
        for dish_data in menu_dishes_data:
            MenuDish.objects.create(menu=instance, **dish_data)

        return instance
