from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CategorySerializer
from .models import Category
from rest_framework import permissions

# Create your views here.
class CategoryListAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class CategoryRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter()
