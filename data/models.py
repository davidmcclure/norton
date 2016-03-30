from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Anthology(models.Model):

    title = models.CharField(max_length = 200)
    year = models.IntegerField()

    def __str__(self):
        return self.title

class Author(models.Model):

    first_name = models.CharField(max_length=20, null = True, blank = True)
    last_name = models.CharField(max_length=200, null = True, blank = True)
    birth_year = models.IntegerField(null = True)
    death_year = models.IntegerField(null = True)
    circa = models.BooleanField(default = False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Work(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author')
    parent = models.ForeignKey('Work', null = True, blank = True)

    def __str__(self):
        return self.title + ' by ' + str(self.author)

    def clean(self):
        pass
