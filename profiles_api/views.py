from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """
    Test API view
    """
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
