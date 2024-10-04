from rest_framework import viewsets

from ..models.menu import Menu
from ..serializers.ser_menu import MenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
