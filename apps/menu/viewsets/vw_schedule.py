from rest_framework import viewsets

from ..models.schedule import Schedule
from ..serializers.ser_schedule import ScheduleSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer