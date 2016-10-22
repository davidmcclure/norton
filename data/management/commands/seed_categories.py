

from django.core.management.base import BaseCommand

from data.models import Gender, Genre, Race


class Command(BaseCommand):

    help = 'Seed gender, genre, and race categories.'

    def handle(self, *args, **kwargs):
        Genre.seed()
        Gender.seed()
        Race.seed()
