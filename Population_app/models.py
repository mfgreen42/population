from django.db import models

# Create your models here.
class Population(models.Model):
    name=models.CharField(max_length=255)
    latitude=models.DecimalField(max_digits=19, decimal_places=4, null=True)
    longitude=models.DecimalField(max_digits=19, decimal_places=4, null=True)
    country=models.CharField(max_length=255)
    population=models.IntegerField()
    is_capital=models.BooleanField(null=True)