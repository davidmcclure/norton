

from django.db import models
from django.core.exceptions import ValidationError


class Work(models.Model):

    title = models.CharField(
        max_length=200,
    )

    author = models.ForeignKey(
        'Author',
        null=True,
    )

    parent = models.ForeignKey(
        'Work',
        null=True,
        blank=True,
    )

    anthologies = models.ManyToManyField(
        'Anthology',
    )

    class Meta:
        unique_together = ('title', 'author', 'parent')

    def __str__(self):

        """
        Include the parent title in the admin listing.
        """

        byline = self.title + ' by ' + str(self.author)

        if self.parent:
            byline += ' [' + self.parent.title + ']'

        return byline

    def clean(self):

        """
        - Ensure that the parent has the same author.
        - Block duplicate title / author pair.
        """

        # Ensure that the parent has the same author.
        if self.parent and self.parent.author != self.author:
            raise ValidationError(
                'The parent work must have the same author.'
            )

        # Block duplicate title / author.
        if not self.parent:

            existing = (
                Work.objects
                .filter(title=self.title, author=self.author)
                .first()
            )

            if existing and existing.id != self.id:
                raise ValidationError(
                    'A work with that title and author already exists.'
                )
