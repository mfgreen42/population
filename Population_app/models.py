from django.db import models

# Create your models here.
class Population(models.Model):
    name=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    population=models.IntegerField()
    limit=models.IntegerField()
