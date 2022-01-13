from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from social_auth.serializers import GoogleSocialAuthSerializes


class GoogleSocialAuthView(GenericAPIView):
    serializer_class = GoogleSocialAuthSerializes

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data['auth_token'])
        return Response(data, status=status.HTTP_200_OK)
