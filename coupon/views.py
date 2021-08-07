from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CouponSerializer
from .models import Coupon
from rest_framework import permissions

# Create your views here.
class CouponListAPIView(ListCreateAPIView):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class CouponRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter()