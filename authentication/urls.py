from django.urls import path
from .views import RegisterView, EmailVerifyView, LoginView, LogoutView, RegisterListAPIView, RegisterRetrieveAPIView, TokenVerifyView, CouponVerifyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email_verify/', EmailVerifyView.as_view(), name='email_verify'),
    path('token_verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('coupon_verify/', CouponVerifyView.as_view(), name='coupon_verify'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('', RegisterListAPIView.as_view(), name='register'),
    path('register/<int:id>', RegisterRetrieveAPIView.as_view(), name='register')
]
