

from django.db import models

from django_countries.fields import CountryField

from localflavor.gb.gb_regions import GB_NATIONS_CHOICES


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
        blank=True,
    )

    gb_country = models.CharField(
        max_length=200,
        verbose_name='Great Britain Country',
        choices=GB_NATIONS_CHOICES,
        null=True,
        blank=True,
    )

    genre = models.ManyToManyField(
        'Genre',
        blank=True,
    )

    race = models.ManyToManyField(
        'Race',
        verbose_name='Race / Ethnicity',
        blank=True,
    )

    gender = models.ForeignKey(
        'Gender',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    notes = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
