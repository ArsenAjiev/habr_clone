from django.test import TestCase
from post.models import Category


class TestCategoryModel(TestCase):

    def test_create_category(self):
        """
        add category instance in Category model
        """
        category_1 = Category.objects.create(title='category')
        self.assertEqual(category_1.title, 'category')

    def test_delete_category(self):
        """
        delete category instance from Category model
        """
        category_1 = Category.objects.create(title='category')
        category_1.delete()
        category_model = Category.objects.all()
        self.assertQuerysetEqual(category_model, [])
