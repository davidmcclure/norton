

from django.db import models

from .category import Category


class Genre(Category):

    DEFAULTS = [
        'Poetry',
        'Novel',
        'Drama',
        'Theory / criticism',
        'Essay',
        'Short fiction',
    ]
