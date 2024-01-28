from rest_framework import serializers
from amicci_app.models import Category, Vendor, Retailer, Briefing


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name']


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ['id', 'name', 'vendors']


class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = ['id', 'name', 'retailer', 'responsible', 'category', 'release_date', 'available']
