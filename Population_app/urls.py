from django.urls import path
from . import views

urlspatterns = [
    [path('', views.population_list)]
    path('<int:pk>/', views.population_detail)
]