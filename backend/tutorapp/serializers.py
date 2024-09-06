# serializers => converts complex data types (djangos model instances) into other content types that can be easily rendered into a response
# serializers -> handles validation of data incoming from request. Ensures data is in required format & constraints (rules for data in table)

from django.contrib.auth.models import User
# serializer, takes the python object (User ^), and converts it into JSON data -> so can be used with other applications
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Serializer:
        model = User
        fields = ["id", "username", "password"]

        def create(self, validated_data):
            