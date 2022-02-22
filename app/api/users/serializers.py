from django.contrib.auth.models import User
from rest_framework import serializers


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "date_joined", "username", "is_staff", "is_active")
