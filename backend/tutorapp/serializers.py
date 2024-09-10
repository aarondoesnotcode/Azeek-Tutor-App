# serializers => converts complex data types (djangos model instances) into other content types that can be easily rendered into a response
# serializers -> handles validation of data incoming from request. Ensures data is in required format & constraints (rules for data in table)

from django.contrib.auth.models import User
# serializer, takes the python object (User ^), and converts it into JSON data -> so can be used with other applications
from rest_framework import serializers
from .models import Booking, Availability


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        # write_only set to true -> so we can write the password, but not read the password in JSON (for privacy)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# creating a serializer for custom models
    class BookingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Booking
            fields = {"student", "time_duration", "date"}
            extra_kwargs = {"student": {"read_only": True}}
            