from django.shortcuts import render

# Create your views here.
# blog/views.py
from rest_framework import viewsets, permissions
from .models import Blog
from .serializers import BlogV1Serializer, BlogV2Serializer
from .throttles import PostRateThrottle

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [PostRateThrottle]

    def get_queryset(self):
        return Blog.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return BlogV1Serializer
        elif self.request.version == 'v2':
            return BlogV2Serializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


def get_serializer_class(self):
    if self.request.version == 'v1':
        return BlogV1Serializer
    elif self.request.version == 'v2':
        return BlogV2Serializer
    return BlogV1Serializer  # fallback

# blog/views.py
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
