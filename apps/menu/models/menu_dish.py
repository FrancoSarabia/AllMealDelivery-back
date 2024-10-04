from django.db import models

from .menu import Menu
from .dish import Dish

class MenuDish(models.Model):
    _id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dish.name} in {self.menu.name}"