from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloAPIView(APIView):
    """
    Test API view
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        Returns a list of APIView features
        """
        api_view = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to the traditional Django View',
            'Gives the most control over the application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hi there!',
                         'api_view': api_view})

    def post(self, request):
        """
        Creates Hello message with name
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  # primary key of the obj to be updated
        """
        Updates an object
        """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """
        Performs partial update of an object
        """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        Delete an object
        """
        return Response({'method': 'DELETE'})
