from django.urls import path
from .views import CouponListAPIView, CouponRetrieveAPIView

urlpatterns = [
    path('', CouponListAPIView.as_view(), name='coupon'),
    path('<int:id>', CouponRetrieveAPIView.as_view(), name='coupon')
]