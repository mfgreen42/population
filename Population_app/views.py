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
#get all cities    
    if request.method == 'GET':
        population = Population.objects.all()
        serializer = PopulationSerializer(population, many = True)
        return Response(serializer.data)
#add a new city    
    elif request.method == 'POST':
        serializer = PopulationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
#get city by ID, I think I'm going to use this to get a random city. How many cities in API?
#choose random number and get city by that ID  
@api_view(['GET'])
def population_detail(request, pk):
    population = get_object_or_404(Population, pk=pk)
    if request.method == 'GET':
        serializer = PopulationSerializer(population)
        return Response(serializer.data)