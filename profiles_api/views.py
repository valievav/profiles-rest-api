from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """
    Test API ViewSet
    """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """
        Return Hello message
        """

        viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello',
                         'viewset': viewset})

    def create(self, request):
        """
        Creates new hello message
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name} :)"
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Gets object by its ID
        """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """
        Updates object
        """
        return Response({'http_method}': 'PUT'})

    def partial_update(self, request, pk=None):
        """
        Updates part of the object (e.g, field)
        """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """
        Removes objects
        """
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Creates and updates user profile
    """

    # create User Profile viewsets
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()  # creates all viewsets for user automatically

    # handle permissions
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnRecord,)

    # allow profile search
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """
    Creates user authentication tokens
    """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES  # to be visible in browseable api (easy to test)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """
    Creates, read and updates profile feed items
    """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnRecord,  # user can update only its status
        IsAuthenticated  # make API available only for authenticated users
    )

    def perform_create(self, serializer):
        """
        Sets the user profile to the logged in user
        """
        serializer.save(user_profile=self.request.user)


class BlogPostView(viewsets.ModelViewSet):
    # lookup_field = 'pk'
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.BlogPost
    permission_classes = (permissions.UpdateOwnRecord,
                          IsAuthenticated,)
