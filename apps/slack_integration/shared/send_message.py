from rest_framework.response import Response
from rest_framework import status
import os

from django.http import JsonResponse
import requests
import json

class Message:
    def send_slack_message(data):
          
        url = "https://slack.com/api/chat.postMessage"
        
        headers = {
            "Authorization": f"Bearer {os.environ.get("TOKEN")}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            print("Mensaje enviado correctamente")
        else:
            print(f"Error al enviar mensaje: {response.status_code}, {response.text}")
            
        return data