

from django.contrib import admin

from data.models import Author, Work, Anthology, Genre, Race

from .author_admin import AuthorAdmin
from .work_admin import WorkAdmin


admin.site.register(Author, AuthorAdmin)
admin.site.register(Anthology)
admin.site.register(Work, WorkAdmin)
admin.site.register(Genre)
admin.site.register(Race)
