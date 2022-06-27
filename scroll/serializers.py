from rest_framework import serializers
from .models import UserPostModel


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostModel
        fields = ['title', 'image', 'date']
