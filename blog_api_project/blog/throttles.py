# blog/throttles.py
from rest_framework.throttling import UserRateThrottle

class PostRateThrottle(UserRateThrottle):
    scope = 'post_blog'
