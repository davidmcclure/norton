from django.db import models

# Create your models here.
class Anthology(models.Model):

    title = models.CharField(max_length = 200)
    year = models.IntegerField()

    def __str__(self):
        return self.title

class Category(models.Model):

    anthology = models.ForeignKey('Anthology', null = True)
    parent = models.ForeignKey('Category', null = True, blank = True)
    label = models.CharField(max_length = 200)

    def __str__(self):
        return self.label

    @property
    def parent_anthology(self):
        if self.anthology:
            return self.anthology
        else:
            return self.parent.anthology

class Author(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_year = models.IntegerField(null = True)
    death_year = models.IntegerField(null = True)
    circa = models.BooleanField(default = False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
