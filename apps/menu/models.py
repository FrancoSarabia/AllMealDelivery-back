from django.db import models

# Create your models here.
from .models.menu import Menu
from .models.schedule import Schedule
from .models.dish import Dish
from .models.dish_type import DishType
from .models.menu_dish import MenuDish
from .models.order import Order