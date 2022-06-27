from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response

from .models import UserPostModel
from .serializers import UserPostSerializer


class UserPostView(viewsets.ModelViewSet):
    queryset = UserPostModel.objects.all()
    serializer_class = UserPostSerializer

    def create(self, request, *args, **kwargs):
        users = request.data

        new_users = UserPostModel.objects.create(title=users['title'], image=users['image'])

        new_users.save()

        serializer = UserPostSerializer(new_users)
        return Response(serializer.data)
