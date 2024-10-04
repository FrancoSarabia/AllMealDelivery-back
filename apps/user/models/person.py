from django.db import models

class Person(models.Model):
    _id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    rut = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        db_table = "person"
        