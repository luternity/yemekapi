from django.shortcuts import render

from apps.yemekler.models import FoodCategory, Food
from apps.api.serializers import FoodCategorySerializer, FoodSerializer

from rest_framework import viewsets

class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows food to be viewed or edited.
    """
    queryset = Food.objects.active()
    serializer_class = FoodSerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows food categories to be viewed or edited.
    """
    queryset = FoodCategory.objects.active()
    serializer_class = FoodCategorySerializer
