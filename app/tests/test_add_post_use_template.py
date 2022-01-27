import pytest

from django.contrib.auth.models import User
from django.test import Client

from post.models import Post


# add post use template 'add_post'
@pytest.mark.django_db
class TestPost:
    def test_index_view(self):
        client = Client()

        response = client.get("/")
        assert response.status_code == 200

    def test_notes_add_view(self):
        client = Client()

        # create user
        user = User.objects.create(username="test", email="test@test.com", password="test")
        client.force_login(user)

        # add post use template
        response = client.post("/add_post/", {"title": "some title", "text": "some text"})
        assert response.status_code == 302
        assert Post.objects.count() == 1
