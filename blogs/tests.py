from django.test import TestCase

from directors.models import Company
from .models import *


class Test_create_Post(TestCase):
    """
    CREATING DB FOR TEST CASE USE
    """

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(
            username="test_user1",
            password="123456789",
            email="admin@gmail.com",
            first_name="first",
            last_name="last",
            other_name="other",
            phone_number="+2346899494",
            user_type=1,
        )
        test_company = Company.objects.create(name="Anchorsoft Academy", company_tracking_id="233437678468668")
        test_hrm = Director.objects.create(user_id=1, company_id=1)
        test_post = Post.objects.create(
            director_id=1,
            author_id=1,
            title="The New Life Career",
            content="The New Life Career",
            status="published",
            slug="the-new-life",
        )

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        author = f"{post.author}"
        director = f"{post.director}"
        title = f"{post.title}"
        content = f"{post.content}"
        status = f"{post.status}"

        self.assertEqual(author, 'first last')
        self.assertEqual(title, "The New Life Career")
        self.assertEqual(content, "The New Life Career")
        self.assertEqual(status, "published")
        self.assertEqual(str(post), "The New Life Career")
