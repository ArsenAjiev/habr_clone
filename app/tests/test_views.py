from django.test import RequestFactory
from django.urls import reverse
from post.views import index, profile, post_detail
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from post. models import Post, Comment
from django.test import Client
import pytest


@pytest.mark.django_db
class TestViews:

    def test_index_view(self):
        path = reverse('home')
        # RequestFactory()  позволяет создавать фиктивные объекты Request для использования в тестировании.
        request = RequestFactory().get(path)
        response = index(request)
        assert response.status_code == 200



    # Тестовый клиент (для обучения)
    def test_client_view(self):

        c = Client()
        # Следует указывать путь из URL без домена c.get('/login/')
        response = c.post('/accounts/register/', {'username': 'john', 'password': 'smith'})
        print(type(response))
        print(response.status_code)

        response2 = c.get(reverse('home'))
        print(type(response2))
        print(response2.content)
        # 200

        # создать пользователя – использовать метод create_user():
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        print(user)
        # john
        print(c.login(username='john', email='lennon@thebeatles.com',  password='johnpassword'))
        # True






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



