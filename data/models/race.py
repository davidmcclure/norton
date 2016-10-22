

from django.db import models

from .category import Category


class Race(Category):

    DEFAULTS = [
        'East Asian',
        'South Asian',
        'Other Asian',
        'Black or African American',
        'Hispanic or Latino',
        'Middle Eastern',
        'Native American, American Indian, or Alaska Native',
        'Native Hawaian or other Pacific Islander',
        'White or European American',
        'Jewish',
    ]

    class Meta:
        verbose_name_plural = 'Racial categories'
