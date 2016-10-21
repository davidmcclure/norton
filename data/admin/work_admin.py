

from urllib.parse import urlencode

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .work_form import WorkForm


class WorkAdmin(admin.ModelAdmin):

    form = WorkForm

    search_fields = ['title', 'author__name']

    def response_add(self, request, obj, post_url_continue=None):

        """
        On "Save and add another," pre-populate author and anthologies.
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
            url = reverse("admin:data_work_changelist")
            return HttpResponseRedirect(url)
