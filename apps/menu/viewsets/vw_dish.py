from rest_framework import viewsets

from ..models.dish import Dish
from ..serializers.ser_dish import DishSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer