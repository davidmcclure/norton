

from django.db import models

from django_countries.fields import CountryField


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

    birth_death_circa = models.BooleanField(
        verbose_name='Birth / death dates are approximate.',
        default=False,
    )

    country = CountryField(
        null=True,
    )

    genres = models.ManyToManyField(
        'Genre',
    )

    race = models.ManyToManyField(
        'Race',
    )

    def __str__(self):
        return self.name
