from django.urls import path

from .views import PayAPIView

urlpatterns = [
    path('pay', PayAPIView.as_view(), name='api_pay'),
]
