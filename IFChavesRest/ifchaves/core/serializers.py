from rest_framework import serializers
from .models import Admin, User, Key, Lending

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'user', 'password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'registry', 'email']

class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ['id', 'keyNumber', 'block', 'classroom', 'status']

class LendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = ['id', 'keyId', 'userId', 'date', 'time', 'status']