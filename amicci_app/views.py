from rest_framework import viewsets
from amicci_app.serializers import CategorySerializer, VendorSerializer, RetailerSerializer, BriefingSerializer
from amicci_app.models import Category, Vendor, Retailer, Briefing

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
    permission_classes = []


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all().order_by('-created_at')
    serializer_class = VendorSerializer
    permission_classes = []


class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all().order_by('-created_at')
    serializer_class = RetailerSerializer
    permission_classes = []


class BriefingViewSet(viewsets.ModelViewSet):
    queryset = Briefing.objects.all().order_by('-created_at')
    serializer_class = BriefingSerializer
    permission_classes = []
