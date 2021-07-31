from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ModulesSerializer
from .models import Modules
from rest_framework import permissions

# Create your views here.
class ModulesListAPIView(ListCreateAPIView):
    serializer_class = ModulesSerializer
    queryset = Modules.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class ModulesRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ModulesSerializer
    queryset = Modules.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter()
