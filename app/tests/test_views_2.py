from django.test import TestCase, Client
from django.urls import reverse
from post.models import Post, Category, Comment
from django.contrib.auth.models import User
import json


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        self.category_1 = Category.objects.create(title='category')
        self.post_1 = Post.objects.create(
            author=self.user,
            title='description',
            text='some text',
            image='461-200x200.jpg',
            category=self.category_1)

        self.index_url = reverse('home')
        self.detail_url = reverse('post_detail', kwargs={'post_pk': self.post_1.id})

    # index view
    def test_index(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # post detail view
    def test_post_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')















