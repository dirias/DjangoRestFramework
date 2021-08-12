from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """API View de prueba"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retorna una lis de característica del APIView"""
        an_apiview = [
            'Usamos métodos HTTP como funciones (get, post, patch, put delete)',
            'Es similar a una vistra tradiional de Django',
            'Nos de el mayour control sobre la lógica de nuetra aplicación',
            'Está mapeado manualmente a los URLs',
        ]
        #convierte la info en formato json pero tiene que ser una lista o diccionario
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Crea un mensaje con el nombre"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'Message': message})
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Maneja actualizar un objeto"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Maneja actualización parcial de un objeto"""
        return  Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Borra un objeto"""
        return  Response({'method': 'DELETE'})
