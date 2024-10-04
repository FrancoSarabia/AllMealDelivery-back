from rest_framework.routers import DefaultRouter
from django.urls import path, re_path

from .views import send_slack_message

urlpatterns = [
    re_path(r'^send-message/$', send_slack_message),
]
