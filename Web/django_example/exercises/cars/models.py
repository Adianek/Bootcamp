from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=50)
    year = models.IntegerField()