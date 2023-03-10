from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Serializer convert from json to dictionary object and vice-versa
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "groups", "last_login", "date_joined"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name"]
