from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from post.views import index, no_permission, CreatePost, profile, post_detail
import pytest
from django.contrib.auth.models import User
from mixer.backend.django import mixer
from post.models import Post

@pytest.mark.django_db
class TestViews:


    def test_index_view(self):
        # 1 Every test needs access to the request factory.
        self.factory = RequestFactory()
        print('\n', self.factory)
        #  <django.test.client.RequestFactory object at 0x7f8aefcc5610>

        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        print('\n', self.user)
        #  jacob

        self.post = Post(author=self.user,
                         title='description',
                         text='qwertry',
                         image='461-200x200.jpg')
        self.post.save()

        # 2 Create an instance of a GET request.
        request = self.factory.get('')
        print('\n', request)
        #   <WSGIRequest: GET '/'>

        # 3 logged-in user by setting request.user manually.
        request.user = self.user
        print('\n', request.user)
        # jacob

        # 4 an AnonymousUser instance.
        request.user = AnonymousUser()
        print('\n', request.user)
        #  AnonymousUser

        # 5 Test index()
        response = index(request)
        print('\n', response)
        #   <HttpResponse status_code=200, "text/html; charset=utf-8">


        #  Test profile()
        response = profile(request)
        print('\n', response)
        #   <HttpResponse status_code=200, "text/html; charset=utf-8">


        #  Test post_detail()
        response = post_detail(request, post_pk=1)
        print('\n', response)
        #   <HttpResponse status_code=200, "text/html; charset=utf-8">




        # 6 Use this syntax for class-based views.
        response = CreatePost.as_view()(request)
        print('\n', response)
        #  <TemplateResponse status_code=200, "text/html; charset=utf-8">

        assert User.objects.count() == 1



















        # path = reverse('home')
        # # RequestFactory()  позволяет создавать фиктивные объекты Request для использования в тестировании.
        # request = RequestFactory().get(path)
        # print('\n', request)
        # response = index(request)
        # print('\n', response)
        # assert response.status_code == 200






    # def test_post_detail_view(self):
    #     user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    #     mixer.blend('post.Post', author=user)
    #     path = reverse('post_detail', kwargs={'post_pk': 1})
    #     # RequestFactory()  позволяет создавать фиктивные объекты Request для использования в тестировании.
    #
    #
    #     request = RequestFactory(author=user).get(path)
    #     response = post_detail(request, post_pk=1)
    #     assert response.status_code == 200

    # Тестовый клиент (для обучения)
    # def test_client_view(self):
    #
    #     c = Client()
    #     # Следует указывать путь из URL без домена c.get('/login/')
    #     response = c.post('/accounts/register/', {'username': 'john', 'password': 'smith'})
    #     print(type(response))
    #     print(response.status_code)
    #
    #     response2 = c.get(reverse('home'))
    #     print(type(response2))
    #     print(response2.content)
    #     # 200
    #
    #     # создать пользователя – использовать метод create_user():
    #     user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    #     print(user)
    #     # john
    #     print(c.login(username='john', email='lennon@thebeatles.com',  password='johnpassword'))
    #     # True












    # def test_post_detail_view(self):
    #     user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    #     mixer.blend('post.Post', author=user)
    #     path = reverse('post_detail', kwargs={'post_pk': 1})
    #     # RequestFactory()  позволяет создавать фиктивные объекты Request для использования в тестировании.
    #
    #
    #     request = RequestFactory(author=user).get(path)
    #     response = post_detail(request, post_pk=1)
    #     assert response.status_code == 200












# from datetime import date, timedelta
#
# from django.contrib.auth import get_user_model, authenticate
# from django.contrib.auth.models import User
# from django.test import TestCase
# from post.models import Post
#
#
# class SigninTest(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
#         self.user.save()
#     def tearDown(self):
#         self.user.delete()
#     def test_correct(self):
#         user = authenticate(username='test', password='12test12')
#         self.assertTrue((user is not None) and user.is_authenticated)
#     def test_wrong_username(self):
#         user = authenticate(username='wrong', password='12test12')
#         self.assertFalse(user is not None and user.is_authenticated)
#     def test_wrong_pssword(self):
#         user = authenticate(username='test', password='wrong')
#         self.assertFalse(user is not None and user.is_authenticated)
#
#
#
# class TaskTest(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
#         self.user.save()
#         self.timestamp = date.today()
#         self.post = Post(author=self.user,
#                          title='description',
#                          text='qwertry')
#         self.post.save()
#     def tearDown(self):
#         self.user.delete()
#     def test_read_task(self):
#         self.assertEqual(self.post.author, self.user)
#         self.assertEqual(self.post.title, 'description')
#         self.assertEqual(self.post.text, 'qwertry')
#     def test_update_task_description(self):
#         self.post.title = 'new description'
#         self.post.save()
#         self.assertEqual(self.post.title, 'new description')













# import pytest
# from django.contrib.auth.models import User
# from django.urls import reverse
#
#
# @pytest.mark.django_db
# def test_user_create():
#   User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#   assert User.objects.count() == 1
#
#
#
#
# @pytest.mark.django_db
# def test_view(client):
#    url = reverse('home')
#    response = client.get(url)
#    assert response.status_code == 200




















# @pytest.mark.django_db
# def test_my_user():
#     user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#     me = User.objects.get(username='john')
#     print(me.username)
#     assert me.username == 'john'

