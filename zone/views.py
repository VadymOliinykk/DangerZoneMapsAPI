from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from zone.models import Zone
from zone.serializers import ZoneListSerializer, ToShowZoneListSerializer
from rest_framework import permissions


class ZoneListAPIView(ListCreateAPIView):
    serializer_class = ZoneListSerializer
    queryset = Zone.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, is_showing=False)


class ToShowZoneListAPIView(ListAPIView):
    serializer_class = ToShowZoneListSerializer
    queryset = Zone.objects.filter(is_showing=True)
    permission_classes = (permissions.IsAuthenticated,)
