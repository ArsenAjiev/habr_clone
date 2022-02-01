from django.test import TestCase
from django.contrib.auth.models import User
from post.models import Post, Category
from django.urls import reverse


class PostIndexView(TestCase):

    def test_no_post(self):
        """
        If no post exist.

        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Posts")
        self.assertQuerysetEqual(response.context['post'], [])

    def test_add_post(self):
        """
        Add post
        """
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        category_1 = Category.objects.create(title='category')
        Post.objects.create(
            author=self.user,
            title='description',
            text='some text',
            image='461-200x200.jpg',
            category=category_1)
        response = self.client.get(reverse('home'))
        self.assertQuerysetEqual(
            response.context['post'],
            ['<Post: description>']
        )
        self.assertEqual(response.status_code, 200)

    def test_add_two_post(self):
        """
        Add post
        """
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        category_1 = Category.objects.create(title='category')
        Post.objects.create(
            author=self.user,
            title='description',
            text='some text',
            image='461-200x200.jpg',
            category=category_1)
        Post.objects.create(
            author=self.user,
            title='description2',
            text='some text2',
            image='461-200x200.jpg',
            category=category_1)
        response = self.client.get(reverse('home'))
        self.assertQuerysetEqual(
            response.context['post'],
            ['<Post: description2>', '<Post: description>']
        )
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        """
        Methods construct a URL from the given name and make
        a HTTP request to the created URL,
        then checks the status code of the request
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Method checks if the correct template
        is loaded when the specified path is visited.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
