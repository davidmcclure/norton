

from django.db import models


class Race(models.Model):

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

    name = models.CharField(
        unique=True,
        max_length=200,
    )

    class Meta:
        verbose_name_plural = 'Racial categories'

    def __str__(self):
        return self.name
