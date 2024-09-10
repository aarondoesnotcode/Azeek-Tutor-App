from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Booking, Availability

# Create your views here.

class BookingCreate(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    # cannot go through to this route, unless validated (valid JWT token)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(student=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(student=self.request.user)
        else:
            print(serializer.errors)

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
