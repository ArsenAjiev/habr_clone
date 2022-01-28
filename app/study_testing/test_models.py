from mixer.backend.django import mixer
import pytest
from post.models import Post, Comment


@pytest.mark.django_db
def test_add_model_Post():
    post = mixer.blend('post.Post', title="some text")
    print(post.image)
    assert post.title == "some text"
    # test coverage for class' __str__
    assert str(post) == "some text"


@pytest.mark.django_db
def test_add_model_Comment():
    comment = mixer.blend('post.Comment', text="some comment")
    print(comment.text)
    assert comment.text == "some comment"
    # test coverage for class' __str__
    assert str(comment) == "some comment"
