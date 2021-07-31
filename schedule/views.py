from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ScheduleSerializer
from .models import Schedule
from rest_framework import permissions

# Create your views here.
class ScheduleListAPIView(ListCreateAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class ScheduleRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter()
