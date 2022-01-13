import random

from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from Backend2 import settings
from user.models import User


def generate_username(name):
    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, name):
    filtered_users_by_email = User.objects.filter(email=email)

    if filtered_users_by_email.exists():
        if provider == filtered_users_by_email[0].auth_provider:
            registered_user = authenticate(email=email, password=settings.GOOGLE_CLIENT_SECRET)

            return {
                'username': registered_user.username,
                'email': registered_user.email,
                'tokens': registered_user.tokens(),
            }

        else:
            raise AuthenticationFailed("AAA")

    else:
        user = {
            'username': generate_username(name), 'email': email, 'password': settings.GOOGLE_CLIENT_SECRET
        }
        user = User.objects.create_user(**user)
        user.auth_provider = provider
        user.save()
        new_user = authenticate(email=email, password=settings.GOOGLE_CLIENT_SECRET)

        return {
            'username': new_user.username,
            'email': new_user.email,
            'tokens': new_user.tokens(),
        }
