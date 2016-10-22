

from django.db import models

from .category import Category


class Gender(Category):

    DEFAULTS = [
        'Male',
        'Female',
        'Other',
    ]

    class Meta:
        verbose_name_plural = 'Gender categories'
