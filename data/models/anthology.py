

from django.db import models


class Anthology(models.Model):

    title = models.CharField(
        max_length=200,
    )

    year = models.IntegerField()

    class Meta:
        verbose_name_plural = 'anthologies'

    def __str__(self):
        return self.title
