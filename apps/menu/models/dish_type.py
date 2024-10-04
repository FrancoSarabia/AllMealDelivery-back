from django.db import models

class DishType(models.Model):
    _id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    name = models.CharField(max_length=150, null=False, default="", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dish_type"