from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Population
from . serializers import PopulationSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def population_list(request):
    
    if request.method == 'GET':
        population = Population.objects.all()
        serializer = PopulationSerializer(population, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PopulationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    