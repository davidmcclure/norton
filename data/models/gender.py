

from django.db import models


class Gender(models.Model):

    name = models.CharField(
        unique=True,
        max_length=200,
    )

    class Meta:
        verbose_name_plural = 'Gender categories'

    def __str__(self):
        return self.name
