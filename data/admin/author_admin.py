

from django.contrib import admin

from .author_form import AuthorForm


class AuthorAdmin(admin.ModelAdmin):

    form = AuthorForm

    search_fields = ['name']
