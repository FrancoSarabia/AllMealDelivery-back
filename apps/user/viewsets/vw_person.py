from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from ..models.person import Person 
from ..models.employee import Employee
from ..serializers.ser_person import PersonSerializer
from ..serializers.ser_employee import EmployeeSerializer
from ..serializers.ser_user import UserSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            try:
                # CREACIÓN DE PERSONA
                person_serializer = self.get_serializer(data=request.data.get('person'))
                person_serializer.is_valid(raise_exception=True)
                person = person_serializer.save()
                
                # CREACIÓN DE USUARIO
                user_data = request.data.get('user')
                if not user_data:
                    transaction.set_rollback(True)
                    return Response({"error": "User data is required"}, status=status.HTTP_400_BAD_REQUEST)
                
                user_serializer = UserSerializer(data=user_data)
                user_serializer.is_valid(raise_exception=True)
                user = user_serializer.save()
                
                # CREACIÓN DE EMPLEADO
                employee = Employee.objects.create(person=person, user=user)

                employee_serializer = EmployeeSerializer(employee)

                response_data = {
                    'person': person_serializer.data,
                    'user': user_serializer.data,
                    'employee': employee_serializer.data
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            except ValueError as error:
                transaction.set_rollback(True)
                productResult = JsonResponse({"error": str(error)}, safe=True, status=409)
                return productResult

