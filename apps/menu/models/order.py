from django.db import models

from ...user.models.client import Client
from .dish import Dish

class Order(models.Model):
    
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    _id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Order {self.id} by {self.client}"