from rest_framework.routers import DefaultRouter

from .viewsets.vw_profile import ProfileViewSet
from .viewsets.vw_person import PersonViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'people', PersonViewSet, basename='person')

urlpatterns = [
]

urlpatterns += router.urls