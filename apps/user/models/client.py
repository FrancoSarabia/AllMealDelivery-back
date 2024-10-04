from django.db import models
from .person import Person

class Client(models.Model):
    _id = models.CharField(primary_key=True ,max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    name = models.CharField(max_length=255, default='')
    username = models.CharField(max_length=255, default='')
    enterprise = models.CharField(max_length=255, default='')
    
    def __str__(self):
        return f"{self.name}"