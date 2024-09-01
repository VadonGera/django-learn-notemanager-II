from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model

from .serializers import UserSerializer
from .permissions import IsAdminUser


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

