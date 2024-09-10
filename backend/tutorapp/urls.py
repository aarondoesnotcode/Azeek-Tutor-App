from django.urls import path
from . import views

urlpatterns = [
    path("booking/", views.BookingCreate.as_view(), name = "create-booking"),
]