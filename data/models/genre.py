

from django.db import models


class Genre(models.Model):

    DEFAULTS = [
        'Poetry',
        'Novel',
        'Drama',
        'Theory / criticism',
        'Essay',
        'Short fiction',
    ]

    name = models.CharField(
        unique=True,
        max_length=200,
    )

    def __str__(self):
        return self.name
