from django.db import models
# this importing of User, is what allows us to get an instance of the person authenticated
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    # student is linked to the User (through foreign key)
    # related_name -> tells us what field name we put on User that references all the bookings
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings") 
    time_duration = models.IntegerField(choices=[(1, '1 hour'), (2, '2 hours')])
    date = models.DateField()

class Availability(models.Model):
    # unique allows for one entry per date
    date = models.DateField(unique=True)
    is_booked = models.BooleanField(default=False)