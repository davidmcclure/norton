

from django.db import models


class Author(models.Model):

    name = models.CharField(
        unique=True,
        max_length=200,
        null=True,
        blank=True,
    )

    birth_year = models.IntegerField(
        null=True,
        blank=True,
    )

    death_year = models.IntegerField(
        null=True,
        blank=True,
    )

    circa = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.name
