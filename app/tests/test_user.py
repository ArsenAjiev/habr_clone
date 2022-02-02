from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserTestCase(TestCase):

    def setUp(self):  # Python's builtin unittest
        user_a = User(username='cfe', email='cfe@invalid.com', password='123')
        # User.objects.create()
        # User.objects.create_user()
        user_a_pw = 'some_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password(user_a_pw)
        self.user_a = user_a

    def test_user_exist(self):
        user_count = User.objects.all().count()  # int
        self.assertEqual(user_count, 1)  # ==
        self.assertNotEqual(user_count, 0)  # !=

    def test_user_password(self):
        """
        Check_password()
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        self.assertTrue(self.user_a.check_password(self.user_a_pw))
        # or user_a_pw = 'some_password'
        self.assertTrue(self.user_a.check_password('some_password'))

    def test_login_url(self):
        # login_url = '/accounts/login/'
        login_url = reverse('login')
        user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        data = {"username": "jacob", "password": "top_secret"}
        response = self.client.post(login_url, data, follow=True)
        print(response.request)
        self.assertEqual(response.status_code, 200)


















    #  exists() - returns True if the QuerySet contains any results.
    # user_qs = User.objects.filter(username__iexact="cfe")   # iexact - case-insensitive exact match
    # user_exists = user_qs.exists() and user_qs.count() == 1  # bool
    # self.assertTrue(user_exists)  # True/ False
    # print("is_anonymous", user_a.is_anonymous)
    # print("date_joined", user_a.date_joined)
    # print("password", user_a.password)
    # print("last_login", user_a.last_login)
    # print("is_authenticated", user_a.is_authenticated)
    # print("is_superuser", user_a.is_superuser)
    # print(user_a.id)

    # python request - manage.py  runserver
    # self.client.get, self.client.post
    # response = self.client.post(url, {}, follow=True
    # user = User.objects.create_user(
    #     username='jacob', email='jacob@mail.qw', password='top_secret')
    # print("is_authenticated", user.is_active)
    # login_url = reverse('login')
    # # login_url = '/accounts/login/'
    # data = {"username": "jacob", "password": "top_secret"}
    # response = self.client.post(login_url, data, follow=True)
    # print(response.request)
    # response = self.client.get('/accounts/logout/', follow=True)
    # print(response.request)
