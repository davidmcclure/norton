

from django.contrib import admin
from django import forms
from django_select2.forms import Select2Widget

from .models import Author, Work, Anthology


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        widgets = dict(anthologies=Select2Widget)
        fields = '__all__'



class WorkAdmin(admin.ModelAdmin):
    form = WorkForm


# Register your models here.
admin.site.register(Author)
admin.site.register(Anthology)
admin.site.register(Work, WorkAdmin)
