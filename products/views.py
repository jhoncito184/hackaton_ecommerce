from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
from .models import Product
from rest_framework import permissions

# Create your views here.
class ProductListAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class ProductRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter()
