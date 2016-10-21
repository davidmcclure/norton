

from urllib.parse import urlencode

from django.contrib import admin
from django import forms
from django_select2.forms import Select2Widget, Select2MultipleWidget
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Author, Work, Anthology


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = '__all__'
        widgets = dict(
            anthologies=Select2MultipleWidget,
            author=Select2Widget,
            parent=Select2Widget,
        )


class WorkAdmin(admin.ModelAdmin):

    form = WorkForm

    search_fields = ['title', 'author__name']

    def response_add(self, request, obj, post_url_continue=None):

        """
        On "add another," pre-populate author and anthologies.
        """

        if '_addanother' in request.POST:

            url = reverse('admin:data_work_add')

            author_id = request.POST['author']
            anthology_ids = request.POST.getlist('anthologies')

            params = {
                'author': author_id,
                'anthologies': ','.join(anthology_ids),
            }

            url += '?'+urlencode(params)

            return HttpResponseRedirect(url)

        else:
            return HttpResponseRedirect(reverse("admin:data_work_changelist"))



class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Anthology)
admin.site.register(Work, WorkAdmin)
