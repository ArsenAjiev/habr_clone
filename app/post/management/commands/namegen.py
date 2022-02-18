from django.core.management import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    # python help function - display the document
    help = 'name generator'

    def handle(self, *args, **options):
        name = get_random_string(length=10)
        self.stdout.write(name)


