from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        return Response({'mensaje': 'Hola desde response'}, status=status.HTTP_200_OK)