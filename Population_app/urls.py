from django.urls import path
from . import views

urlpatterns = [
    path('', views.population_list)
    # path('<int:pk>/', views.population_detail)
]