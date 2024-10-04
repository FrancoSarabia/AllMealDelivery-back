from rest_framework import viewsets
from ..models.dish_type import DishType
from ..serializers.ser_dish_type import DishTypeSerializer

class DishTypeViewSet(viewsets.ModelViewSet):
    queryset = DishType.objects.all()
    serializer_class = DishTypeSerializer