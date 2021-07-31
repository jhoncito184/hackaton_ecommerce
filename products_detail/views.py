from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductDetailSerializer
from .models import ProductDetail
from rest_framework import permissions

# Create your views here.
class ProductDetailListAPIView(ListCreateAPIView):
    serializer_class = ProductDetailSerializer
    queryset = ProductDetail.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class ProductDetailRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = ProductDetail.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter()
