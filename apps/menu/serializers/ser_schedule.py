from rest_framework import serializers
from ..models.schedule import Schedule
from ..models.menu import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['_id', 'name', 'description']

class ScheduleSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)  # Para devolver los detalles del menú
    menu_id = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all(), source='menu', write_only=True)

    class Meta:
        model = Schedule
        fields = ['_id', 'date', 'start_time', 'end_time', 'menu', 'menu_id']