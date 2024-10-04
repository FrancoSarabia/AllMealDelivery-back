from datetime import datetime
from django.utils import timezone

from ..models.schedule import Schedule

def validate_schedule(menu_id):
    now = timezone.now()
    try:
        # Aquí se valida si el menú está disponible
        schedule = Schedule.objects.get(menu=menu_id, date=timezone.now().date())
    except Schedule.DoesNotExist:
        return {"ok": False,"error": "No hay un horario programado para este menú"}

    # Comparar la hora actual con `start_time` y `end_time` de la tabla `Schedule`
    current_time = now.time()
    
    if schedule.start_time <= current_time <= schedule.end_time:
        return {"ok": True, "error": ""}
    else:
        return {"ok": False, "error": "El menú no está disponible en este horario."}