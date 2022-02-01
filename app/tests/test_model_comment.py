from django.test import TestCase
from django.contrib.auth.models import User
from post.models import Comment, Category, Post

import datetime


class TestCommentModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.qw', password='top_secret')
        category_1 = Category.objects.create(title='category')
        post_1 = Post.objects.create(
            author=self.user,
            title='description',
            text='some text',
            image='461-200x200.jpg',
            category=category_1)
        Comment.objects.create(
            author=self.user,
            text='some comment',
            created=datetime.datetime.now(),
            post=post_1)

    def test_create_comment(self):
        """
        add comment instance in Comment model
        """
        comment_1 = Comment.objects.get(text='some comment')
        self.assertEqual(comment_1.text, 'some comment')

    def test_delete_comment(self):
        """
        delete comment instance from Comment model
        """
        comment_1 = Comment.objects.get(text='some comment')
        comment_1.delete()
        comment_model = Comment.objects.all()
        self.assertQuerysetEqual(comment_model, [])


