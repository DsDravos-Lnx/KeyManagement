from django.shortcuts import render
from rest_framework import viewsets
from .models import Admin, Key, Lending, User
from .serializers import AdminSerializer, KeySerializer, LendingSerializer, UserSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()
    serializer_class = KeySerializer

class LendingViewSet(viewsets.ModelViewSet):
    queryset = Lending.objects.all()
    serializer_class = LendingSerializer
