from django.urls import path
from .views import ScheduleListAPIView, ScheduleRetrieveAPIView

urlpatterns = [
    path('', ScheduleListAPIView.as_view(), name='schedule'),
    path('<int:id>', ScheduleRetrieveAPIView.as_view(), name='schedule')
]
