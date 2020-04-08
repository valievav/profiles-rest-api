from rest_framework import serializers


class HelloSerializer(serializers.Serializer):  # converts data input into Python obj and vice versa
    """
    Serializes a name field to test POST functionality of APIView
    """
    name = serializers.CharField(max_length=10)
