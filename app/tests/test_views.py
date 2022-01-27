from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User

from post.views import index, no_permission, post_detail, profile, CreatePost, register
from post.views import delete_post, delete_comment
from post.models import Post, Comment


import pytest


@pytest.mark.django_db
class TestViews:

    def test_index_view(self):
        path = reverse('home')
        # RequestFactory()  позволяет создавать фиктивные объекты Request для использования в тестировании.
        request = RequestFactory().get(path)
        response = index(request)
        assert response.status_code == 200

    def test_no_permission_view(self):
        path = reverse('no_permission')
        request = RequestFactory().get(path)
        response = no_permission(request)
        assert response.status_code == 200

    def test_post_detail_view(self):
        # create user
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')

        # create Post
        self.post = Post(author=self.user,
                         title='description',
                         text='qwertry',
                         image='461-200x200.jpg')
        # save Post
        self.post.save()

        # path('post_detail/<post_pk>/', post_detail, name='post_detail'),
        path = reverse('post_detail', kwargs={'post_pk': 1})
        print('\n', path)
        #  in this case  /post_detail/1/

        # Когда запрашивается страница, Django создает объект HttpRequest, который содержит различные данные о запросе
        request = RequestFactory().get(path)
        print('\n', request)
        #  <WSGIRequest: GET '/post_detail/1/'>

        # in this case WSGIRequest object needs attribute 'user'
        request.user = self.user
        response = post_detail(request, post_pk=1)
        # check status code
        assert response.status_code == 200
        # check create Post
        assert Post.objects.count() == 1

    def test_profile_view(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        self.post = Post(author=self.user,
                         title='description',
                         text='qwertry',
                         image='461-200x200.jpg')
        self.post.save()
        path = reverse('profile')
        request = RequestFactory().get(path)
        request.user = self.user
        response = profile(request)
        assert response.status_code == 200

    def test_create_post(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        path = reverse('add_post')
        request = RequestFactory().post(path, {"title": "some title", "text": "some text"})
        request.user = self.user
        response = CreatePost.as_view()(request)
        assert response.status_code == 302
        assert Post.objects.count() == 1



    def test_register_view(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        path = reverse('register')
        request = RequestFactory().get(path)
        response = register(request)
        assert response.status_code == 200

    def test_delete_post_view(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        self.post = Post(author=self.user,
                         title='description',
                         text='qwertry',
                         image='461-200x200.jpg')
        self.post.save()
        path = reverse('delete_post', kwargs={'post_pk': 1})
        request = RequestFactory().get(path)
        request.user = self.user
        response = delete_post(request, post_pk=1)
        assert Post.objects.count() == 0
        assert response.status_code == 302




    def test_delete_comment(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        self.post = Post(author=self.user,
                         title='description',
                         text='qwertry',
                         image='461-200x200.jpg')
        self.post.save()
        self.comment = Comment(text='comment', object_id=1, author_id=1, content_type_id=1)
        self.comment.save()
        path = reverse('delete_comment', kwargs={'comm_pk': 1})
        request = RequestFactory().get(path)
        request.user = self.user
        response = delete_comment(request, comm_pk=1)
        assert Comment.objects.count() == 0
        assert response.status_code == 302



    def test_no_permission_delete_comment(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        self.post = Post(author=self.user,
                         title='description',
                         text='qwertry',
                         image='461-200x200.jpg')
        self.post.save()
        self.comment = Comment(text='comment', object_id=1, author_id=1, content_type_id=1)
        self.comment.save()
        path = reverse('delete_comment', kwargs={'comm_pk': 1})
        request = RequestFactory().get(path)
        request.user = AnonymousUser()
        response = delete_comment(request, comm_pk=1)
        assert Comment.objects.count() != 0









