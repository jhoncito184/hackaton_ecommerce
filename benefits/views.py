from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BenefitsSerializer
from .models import Benefits
from rest_framework import permissions

# Create your views here.
class BenefitsListAPIView(ListCreateAPIView):
    serializer_class = BenefitsSerializer
    queryset = Benefits.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class BenefitsRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BenefitsSerializer
    queryset = Benefits.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter()
