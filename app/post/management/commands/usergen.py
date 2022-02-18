from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'DB random user generator'

    def add_arguments(self, parser):
        parser.add_argument('qty', type=int, help='The amount of users to create')

    def handle(self, *args, **kwargs):
        qty = kwargs['qty']

        for i in range(qty):
            username = get_random_string(5)
            password = get_random_string(5)

            User.objects.create(username=username, email='', password=password)

            self.stdout.write('User "%s (%s)" account created!' % (username, password))



