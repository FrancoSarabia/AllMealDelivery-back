from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .viewsets.vw_menu import MenuViewSet
from .viewsets.vw_dish_type import DishTypeViewSet
from .viewsets.vw_dish import DishViewSet
from .viewsets.vw_schedule import ScheduleViewSet
from .viewsets.vw_order import OrderViewSet

router = DefaultRouter()
router.register(r'menus', MenuViewSet, basename='menu')
router.register(r'dishtypes', DishTypeViewSet, basename='dish-type')
router.register(r'dishes', DishViewSet, basename='dish')
router.register(r'schedules', ScheduleViewSet, basename='schedule')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls