from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .resources.json.message_json import JSONElement
from .shared.send_message import Message
from ..menu.models.menu import Menu
from ..menu.serializers.ser_menu import MenuSerializer
from ..menu.models.dish_type import DishType
from ..menu.models.dish import Dish

# Create your views here.
@api_view(['POST'])
def send_slack_message(request):
    message_data = JSONElement.get_json_payload()
    menu_id = request.data.get('menu_id')
    
    try:
        menu = Menu.objects.get(_id=menu_id)
    except Menu.DoesNotExist:
        return Response({'error': 'Menu not found'}, status=404)
    
    serialized_menu = MenuSerializer(menu).data
    slack_json = message_data['blocks']
    slack_json[1]["text"]["text"] = serialized_menu["name"]
    
    dish_types = DishType.objects.all()
    
    # Añadir los platos agrupados por tipo
    for dish_type in dish_types:
        slack_json.append({
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": dish_type.name,
                "emoji": True
            }
        })
        slack_json.append({"type": "divider"})
        # Recuperar los platos por tipo de plato
        dishes = Dish.objects.filter(dish_type=dish_type, menudish__menu=menu)
        
        for dish in dishes:
            slack_json.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{dish.name}*\n:heavy_dollar_sign: {dish.price}\n {dish.description}"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://example.com/{dish.image}",
                    "alt_text": dish.name
                }
            })
            slack_json.append({
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Seleccionar",
                            "emoji": True
                        },
                        "value": str(menu_id) + ' - ' + str(dish._id),
                        "action_id": "actionId-0"
                    }
                ]
            })
    message_data['blocks'] = slack_json
    data = Message.send_slack_message(message_data)
    return Response({'message': 'Menu successfully sended', 'data': data}, status=200)
    