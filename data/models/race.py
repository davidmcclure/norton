

from django.db import models


class Race(models.Model):

    name = models.CharField(
        unique=True,
        max_length=200,
    )

    class Meta:
        verbose_name_plural = 'Racial categories'

    def __str__(self):
        return self.name
