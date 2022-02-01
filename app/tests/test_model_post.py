from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from post.models import Post, Category


class TestPostModel(TestCase):
    def setUp(self):
        # create User
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        # create category
        category_1 = Category.objects.create(title='category')
        # create Post with id = 1
        Post.objects.create(
            author=self.user,
            title='description',
            text='some text',
            image='461-200x200.jpg',
            category=category_1)

    def test_create_post(self):
        """
        add post instance in Post model
        """
        post_1 = Post.objects.get(text='some text')
        self.assertEqual(post_1.text, 'some text')

    def test_get_absolute_url(self):
        """
        get absolute url to post
        http://127.0.0.1:8000/post_detail/post_1.id/
        """
        post_1 = Post.objects.get(text='some text')
        url = reverse('post_detail', args=(post_1.id,))
        response = self.client.get(url)
        self.assertContains(response, post_1.text)

    def test_delete_post(self):
        """
        delete post instance from Post model
        it must be an empty QuerySet
        """
        post_1 = Post.objects.get(text='some text')
        post_1.delete()
        post_model = Post.objects.all()
        self.assertQuerysetEqual(post_model, [])
