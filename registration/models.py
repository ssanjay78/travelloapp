from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

# Created Class to take objects for Testimonials 
class Testimonials(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=50)