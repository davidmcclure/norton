

from django.db import models, IntegrityError


class Category(models.Model):

    DEFAULTS = []

    name = models.CharField(
        unique=True,
        max_length=200,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    @classmethod
    def seed(cls):

        """
        Insert default values.
        """

        for name in cls.DEFAULTS:

            try:
                cls.objects.create(name=name)

            except IntegrityError as e:
                print(e)
