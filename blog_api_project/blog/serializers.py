# blog/serializers.py
from rest_framework import serializers
from .models import Blog

class BlogV1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

class BlogV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'category', 'tags', 'view_count', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at', 'view_count']

# blog/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
