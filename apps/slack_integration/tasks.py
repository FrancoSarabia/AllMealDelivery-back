from celery import shared_task
import requests

@shared_task
def send_scheduled_message():
    url = 'http://localhost:8000/integration/slack/send-message/'
    data = {'message': 'Scheduled message from Celery'}
    
    response = requests.post(url, json=data)
    return response.status_code