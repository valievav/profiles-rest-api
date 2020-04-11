from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):  # converts data input into Python obj and vice versa
    """
    Serializes a name field to test POST functionality of APIView
    """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializes fields for User Profile model
    """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }}

    def create(self, validated_data):
        """
        Create and return new user
        """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """
        Update user account
        """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """
    Serializes profile feed item model
    """

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


class BlogPost(serializers.ModelSerializer):
    class Meta:
        model = models.BlogPost
        fields = ['pk', 'user_profile', 'title', 'content', 'timestamp']
        extra_kwargs = {'user_profile': {'read_only': True}}
