from django.shortcuts import render
from rest_framework import generics
from .serializers import RecipeSerialier
from . import models


class RecipesListView(generics.ListCreateAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = RecipeSerialier

class RecipesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = RecipeSerialier
