

from django.db import models
from django.core.exceptions import ValidationError
from titlecase import titlecase

# Create your models here.
class Anthology(models.Model):

    title = models.CharField(max_length = 200)
    year = models.IntegerField()

    class Meta:
        verbose_name_plural = 'anthologies'

    def __str__(self):
        return self.title

class Author(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True, unique=True)
    birth_year = models.IntegerField(null=True)
    death_year = models.IntegerField(null=True)
    circa = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Work(models.Model):

    # TODO: Unique index on title, author, and parent

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', null = True)
    parent = models.ForeignKey('Work', null = True, blank = True)
    anthologies = models.ManyToManyField('Anthology')

    class Meta:
        unique_together = ('title', 'author', 'parent')

    def __str__(self):
        byline = self.title + ' by ' + str(self.author)
        if self.parent:
            byline += ' (' + self.parent.title + ')'
        return byline

    def clean(self):

        # Ensure that the parent has the same author.
        if self.parent and self.parent.author != self.author:
            raise ValidationError('The parent work must have the same author.')

        # Block duplicate title / author.
        if not self.parent:

            existing = Work.objects.filter(
                title=self.title,
                author=self.author,
            )

            if existing.count() > 0:
                raise ValidationError('A work with that title and author already exists.')
