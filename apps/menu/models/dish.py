from django.db import models

from .dish_type import DishType

class Dish(models.Model):
    _id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name='dishes', null=False, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dish"