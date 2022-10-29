from urllib import response
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from accounts.models import User


class PostTestCase(APITestCase):
    def test_view_posts(self):

        url = reverse("listcreate")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        self.test_user1 = User.objects.create_user(
            username="test_user1",
            password="123456789",
            email="admin@gmail.com",
            first_name="first",
            last_name="last",
            other_name="other",
            phone_number="+2346899494",
            user_type=1,
        )

        data = {
            'title':'New',
            'author':1,
            'content':'New Days Ahead',
            'status':'published',
            'slug':'new-days'
        }

        url = reverse('listcreate')
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
