from rest_framework import serializers
from .models import ProductDetail


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['id', 'product', 'title', 'subtitle', 'content_detail', 'image', 'schedule', 'modules']