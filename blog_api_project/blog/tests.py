from django.test import TestCase

# Create your tests here.
# blog/tests.py
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status
from .models import Blog

class BlogAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_blog_crud_v1(self):
        url = '/api/v1/blogs/'
        # CREATE
        response = self.client.post(url, {'title': 'Blog V1', 'content': 'Content V1'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        blog_id = response.data['id']

        # GET
        response = self.client.get(f'{url}{blog_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Blog V1')

        # UPDATE
        response = self.client.put(f'{url}{blog_id}/', {'title': 'Updated V1', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # DELETE
        response = self.client.delete(f'{url}{blog_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_blog_crud_v2(self):
        url = '/api/v2/blogs/'
        response = self.client.post(url, {'title': 'Blog V2', 'content': 'Content V2', 'category': 'Tech', 'tags': 'Python,API'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        blog_id = response.data['id']

        response = self.client.get(f'{url}{blog_id}/')
        self.assertEqual(response.data['category'], 'Tech')
        self.assertEqual(response.data['tags'], 'Python,API')

    def test_post_throttle(self):
        url = '/api/v1/blogs/'
        for i in range(5):
            response = self.client.post(url, {'title': f'Blog {i}', 'content': 'Test'})
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # 6th post should fail
        response = self.client.post(url, {'title': 'Blog 6', 'content': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
