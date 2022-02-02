from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from post.models import Post, Category, Comment
from django.contrib.auth.models import User, AnonymousUser
from post.views import delete_post, index, profile, CreatePost


class TestView(TestCase):

    def test_index_view(self):
        client = Client()
        user = User.objects.create_user(username='jacob', email='jacob@mail.qw', password='top_secret')
        client.force_login(user)
        category_1 = Category.objects.create(title='category')
        Post.objects.create(
            author=user,
            title='description',
            text='some text',
            image='461-200x200.jpg',
            category=category_1)

        path = reverse('home')
        #  request = RequestFactory().get(path)  # <WSGIRequest: GET '/'>
        #  response = index(path)  # <HttpResponse status_code=200, "text/html; charset=utf-8">
        response = client.get(reverse('home'))
        # print(response.context)
        self.assertQuerysetEqual(response.context['post'], ['<Post: description>'])

    def test_profile_view(self):
        client = Client()
        user = User.objects.create_user(username='jalll', email='jacob@mail.qw', password='top_secret')
        client.force_login(user)
        category_1 = Category.objects.create(title='category')
        Post.objects.create(
            author=user,
            title='description',
            text='some text',
            image='461-200x200.jpg',
            category=category_1)
        path = reverse('profile')
        request = RequestFactory().get(path)
        #  request = RequestFactory().get(path)  # <WSGIRequest: GET '/'>
        #  response = index(path)  # <HttpResponse status_code=200, "text/html; charset=utf-8">
        response = client.get(reverse('profile'))
        # print(response.context)
        # print(response.status_code)

    def test_delete_post_view(self):
        user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        category_1 = Category.objects.create(title='category')
        post = Post(
            author=user,
            title='description',
            text='qwertry',
            image='461-200x200.jpg',
            category=category_1
            )
        post.save()
        print(Post.objects.all())
        path = reverse('delete_post', kwargs={'post_pk': 1})
        request = RequestFactory().get(path)
        request.user = user
        response = delete_post(request, post_pk=1)
        post_count = Post.objects.all().count()  # int
        self.assertEqual(post_count, 0)  # ==
        self.assertNotEqual(post_count, 1)









    # def test_create_post(self):
    #     client = Client()
    #     user = User.objects.create_user(username='jalll', email='jacob@mail.qw', password='top_secret')
    #     client.force_login(user)
    #     category_1 = Category.objects.create(title='category')
    #     path = reverse('add_post')
    #     data = {"title": "some title", "text": "some text", "category": category_1}
    #     response = client.post(path, data, follow=True)
    #     print(Post.objects.all())

