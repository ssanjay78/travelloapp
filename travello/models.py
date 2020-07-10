from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

# Created class to take objects for Destinations
class PlacesData(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

# Created Class to take objects for Testimonials 
class Testimonials(models.Model):
    comment = ArrayField(models.TextField())
    name = ArrayField(models.CharField(max_length=50))
