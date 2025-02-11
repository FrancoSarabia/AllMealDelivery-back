"""
URL configuration for allmeal_delivery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

#from ..apps.user.view.login_view import Login

from apps.user.views import Login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("menu/", include('apps.menu.urls')),
    path("user/", include('apps.user.urls')),
    path("integration/slack/", include('apps.slack_integration.urls')),
    path('', Login.as_view(), name='Login')
]
