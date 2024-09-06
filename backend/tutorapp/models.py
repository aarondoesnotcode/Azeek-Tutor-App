from django.db import models
# this importing of User, is what allows us to get an instance of the person authenticated
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE) # 'User' is an instance of the user currently authenticated
    timeDuration = models.IntegerField(choices=[(1, '1 hour'), (2, '2 hours')])
    date = models.DateField()

class Availability(models.Model):
    # unique allows for one entry per date
    date = models.DateField(unique=True)
    is_booked = models.BooleanField(default=False)