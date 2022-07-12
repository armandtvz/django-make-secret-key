"""
Generate a ``SECRET_KEY`` value for a new Django project/environment.
"""

from django.core.management.utils import get_random_secret_key
from django.utils.crypto import get_random_string


def generate(length=70):
    # https://github.com/django/django/blob/main/django/core/management/utils.py#L77
    # https://github.com/django/django/blob/3e6a3e885336bea43bc42b8fdf8e2401970b7018/django/utils/crypto.py#L50
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    key = get_random_string(length=length, allowed_chars=chars)
    print(key)


if __name__ == '__main__':
    generate()
