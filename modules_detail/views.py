from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ModulesDetailSerializer
from .models import ModulesDetail
from rest_framework import permissions

# Create your views here.
class ModulesDetailListAPIView(ListCreateAPIView):
    serializer_class = ModulesDetailSerializer
    queryset = ModulesDetail.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class ModulesDetailRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ModulesDetailSerializer
    queryset = ModulesDetail.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter()
