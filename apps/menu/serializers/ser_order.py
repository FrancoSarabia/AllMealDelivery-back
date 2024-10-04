# serializers.py
from rest_framework import serializers
from ..models.order import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['_id', 'client', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']