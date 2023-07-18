from rest_framework import serializers
from . models import Population

class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Population
        fields = ["id", "name", "latitude", "longitude", "country", "population", "is_capital"]