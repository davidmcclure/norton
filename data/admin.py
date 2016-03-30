from django.contrib import admin
from .models import Author, Work, Anthology

# Register your models here.
admin.site.register(Author)
admin.site.register(Anthology)
admin.site.register(Work)
