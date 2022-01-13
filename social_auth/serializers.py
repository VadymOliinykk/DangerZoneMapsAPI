from abc import ABC

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from Backend2 import settings
from social_auth import google
from social_auth.register import register_social_user


class GoogleSocialAuthSerializes(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)

        try:
            user_data['sub']
        except:
            raise serializers.ValidationError('Token Invalid')

        if user_data['aud'] != settings.GOOGLE_CLIENT_ID:
            raise AuthenticationFailed("Failed Client Id Check")

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(provider=provider, user_id=user_id, email=email, name=name)
