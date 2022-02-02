from django.test import TestCase
from post.forms import AddCommentForm, PostForm
from django.contrib.auth.models import User
from post.models import Category


class TestForms(TestCase):

    def test_add_comment_form_with_valid_data(self):
        form = AddCommentForm(data={
            "text": "some comment"
        })
        self.assertTrue(form.is_valid())

    def test_add_comment_form_no_data(self):
        form = AddCommentForm(data={})
        self.assertFalse(form.is_valid())
        # form.errors - return an ErrorDict for the data provided for the form
        # in this case 1 field
        self.assertEqual(len(form.errors), 1)

    def test_post_form_with_valid_data(self):
        category_1 = Category.objects.create(title='category')

        form = PostForm(data={
            "title": 'description',
            "text": 'some text',
            "category": category_1,
        })
        self.assertTrue(form.is_valid())

    def test_post_form_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        # form.errors - return an ErrorDict for the data provided for the form
        # in this case 3 field
        self.assertEqual(len(form.errors), 3)
