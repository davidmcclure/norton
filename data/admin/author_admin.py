

from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']
