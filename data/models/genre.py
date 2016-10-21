

from django.db import models


class Genre(models.Model):

    name = models.CharField(
        unique=True,
        max_length=200,
    )

    def __str__(self):
        return self.name
