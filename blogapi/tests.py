from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Post

from django.urls import reverse

class PostTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_Post = Post.objects.create(
            title="rake",
            description="Better for collecting leaves than a shovel.",
        )
        test_Post.save()


    def setUp(self):
        self.client.login(username='testuser1', password="pass")




    def test_Post_model(self):
        post = Post.objects.get(id=1)
        actual_title = str(post.title)
        actual_description = str(post.description)
        self.assertEqual(actual_title, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_post_list(self):
        url = reverse("blog_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

