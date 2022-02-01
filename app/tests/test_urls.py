from django.test import TestCase
from django.urls import reverse, resolve
from post.views import index, post_detail, CreatePost


class TestUrls(TestCase):

    # for function - resolve(url).func
    def test_index_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_post_detail_url_is_resolved(self):
        url = reverse('post_detail',  kwargs={'post_pk': '1'})
        self.assertEqual(resolve(url).func, post_detail)

    # for class  - resolve(url).func.view_class
    def test_add_post_url_is_resolved(self):
        url = reverse('add_post')
        self.assertEqual(resolve(url).func.view_class, CreatePost)


