from django.urls import path

from zone.views import ZoneListAPIView, ToShowZoneListAPIView

urlpatterns = [
    path('', ZoneListAPIView.as_view(), name='zones'),
    path('to_show/', ToShowZoneListAPIView.as_view(), name='to_show_zones'),
]
