

from django.core.management.base import BaseCommand

from data.models import Gender, Genre, Race


class Command(BaseCommand):

    help = 'Seed gender, genre, and race categories.'

    def handle(self, *args, **kwargs):

        for name in Genre.DEFAULTS:
            Genre.objects.create(name=name)

        for name in Gender.DEFAULTS:
            Gender.objects.create(name=name)

        for name in Race.DEFAULTS:
            Race.objects.create(name=name)
