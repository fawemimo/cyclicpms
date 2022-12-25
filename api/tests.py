from urllib import response
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from accounts.models import User
from blogs.models import Post


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

        # root = reverse(('detailcreate'), kwargs={'pk':1})
        # response = self.client.get(url, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_update(self):
        client = APIClient()

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

        self.test_user2 = User.objects.create_user(
            username="test_user2",
            password="1234567890",
            email="admin01@gmail.com",
            first_name="first",
            last_name="last",
            other_name="other",
            phone_number="+2346899494",
            user_type=1,
        )

        test_post_data = Post.objects.create(  
            director=1,       
            title='New',
            author=1,
            content='New Days Ahead',
            status='published',
            slug='new-days'
        )

        client.login(username=self.test_user1.username,password='123456789')

        url = reverse(('listdetail'), kwargs={'pk':1})

        response = client.put(
            url, {
            'id':1,
            'title':'New',
            'author':1,
            'content':'New Days Ahead',
            'status':'published',
            'slug':'new-days'
            },
            format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)