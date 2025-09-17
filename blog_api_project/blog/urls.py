

# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, UserViewSet

router = DefaultRouter()
router.register('blogs', BlogViewSet, basename='blogs')
router.register('users', UserViewSet, basename='users')  # new

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v2/', include(router.urls)),
]
