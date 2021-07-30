from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostulationsSerializer
from .models import Postulations
from rest_framework import permissions

# Create your views here.
class PostulationsListAPIView(ListCreateAPIView):
    serializer_class = PostulationsSerializer
    queryset = Postulations.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class PostulationsRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostulationsSerializer
    queryset = Postulations.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter()
