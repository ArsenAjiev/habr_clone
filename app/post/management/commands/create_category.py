from post.models import Category
from django.core.management.base import BaseCommand
from django.db.utils import Error


class Command(BaseCommand):
    help = 'Create category for DB'

    def handle(self, *args, **kwargs):
        list_category = ['Economy', 'Technology', 'Sport', 'Music']

        for i in list_category:
            try:
                category = Category.objects.create(title=i)
            except Error:
                print('Category "%s" exist' % i)
                continue
            self.stdout.write(self.style.SUCCESS('Successfully created "%s" category' % category))

