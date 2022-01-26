from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
def test_add_model_Post():
    post = mixer.blend('post.Post', text="some text")
    print(post.text)
    assert post.text == "some text"


@pytest.mark.django_db
def test_add_model_Comment():
    comment = mixer.blend('post.Comment', text="some comment")
    print(comment.text)
    assert comment.text == "some comment"
