from django.db import models
from datetime import datetime, timedelta

from .menu import Menu
from datetime import date

def default_start_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)  

class Schedule(models.Model):
    _id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    name = models.CharField(max_length=100, default='')
    start_time = models.TimeField(default=default_start_time)
    end_time = models.TimeField(default=default_start_time)
    date = models.DateField(default=date.today())
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.date}"