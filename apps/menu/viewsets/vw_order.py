from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.http import JsonResponse
import json
import requests

from ..models.order import Order
from ...user.models.client import Client
from ..models.dish import Dish
from ..serializers.ser_order import OrderSerializer
from ..utils.schedule import validate_schedule

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    # ENDPOINT EJECUTADO POR EL WEBHOOK DE SLACK
    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            try:
                payload = json.loads(request.POST.get('payload'))
                action = payload['actions'][0]
                
                try:
                    menu_id = int(action['value'].split(' - ')[0])
                    dish_id = int(action['value'].split(' - ')[1])
                except (IndexError, ValueError):
                    return Response({"error": "Invalid action value format"}, status=status.HTTP_400_BAD_REQUEST)
                
                # VALIDACION DEL RANGO DE TIEMPO DISPONIBLE DEL MENU
                validation = validate_schedule(menu_id)
                if validation == False:
                    requests.post(payload['response_url'], json={"text": validation["error"]})
                    return JsonResponse( {"error": validation["error"]}, safe=True, status=400)
                
                try:
                    dish_data = Dish.objects.get(_id=dish_id)
                except Dish.DoesNotExist:
                    return Response({"error": "Dish not found"}, status=status.HTTP_404_NOT_FOUND)
                
                # Datos del cliente
                user_id = payload['user']['id']
                name = payload['user']['name']
                username = payload['user']['username']
                enterprise = payload['enterprise']
                
                # OBTENCION O CREACION DEL CLIENTE
                client, created = Client.objects.get_or_create(_id=user_id, defaults={
                    '_id': user_id,
                    'name': name,
                    'username': username,
                    'enterprise': '' if enterprise is None else enterprise
                })
                # CREACIÓN DE LA ORDEN
                order = Order(
                    client = client,
                    dish = dish_data
                )
                order.save()
                
                # Enviar una respuesta a Slack
                response_url = payload['response_url']
                requests.post(response_url, json={"text": "Su pedido fue ingresado exitosamente."})
                return Response({"message": "Order created successfully"}, status=status.HTTP_201_CREATED)
            
            except json.JSONDecodeError as e:
                transaction.set_rollback(True)
                print(str(e))
                return JsonResponse({"error": "Invalid JSON payload", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            except ValueError as e:
                transaction.set_rollback(True)
                print(str(e))
                return JsonResponse({"error": str(e)}, status=status.HTTP_409_CONFLICT)

            except Exception as e:
                transaction.set_rollback(True)
                print(str(e))
                return JsonResponse({"error": "An unexpected error occurred", "details": str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)