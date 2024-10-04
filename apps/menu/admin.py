from django.contrib import admin
from ..menu.models.menu import Menu
from ..menu.models.dish import Dish
from ..menu.models.dish_type import DishType
from ..menu.models.order import Order
from ..menu.models.schedule import Schedule
from ..menu.models.menu_dish import MenuDish

# Register your models here.
admin.site.register(Menu)
admin.site.register(Dish)
admin.site.register(DishType)
admin.site.register(Order)
admin.site.register(Schedule)
admin.site.register(MenuDish)