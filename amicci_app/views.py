from django.shortcuts import render
from rest_framework import viewsets
from amicci_app.serializers import CategorySerializer
from amicci_app.models import Category

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
    permission_classes = []