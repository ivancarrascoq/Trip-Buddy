from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Trip(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    destination = models.CharField(validators=[MinLengthValidator(3)], null=False, max_length=100)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    plan = models.CharField(validators=[MinLengthValidator(3)], null=False, max_length=200)

class TripJoined(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)