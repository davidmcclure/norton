

from django.db import models

from .category import Category


class Genre(Category):

    DEFAULTS = [
        'Poetry',
        'Novel',
        'Drama',
        'Personal Essay / Memoir',
        'Essay / Criticism',
        'Short fiction',
    ]
