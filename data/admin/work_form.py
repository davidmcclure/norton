

from django import forms
from django_select2.forms import Select2Widget, Select2MultipleWidget

from data.models import Work


class WorkForm(forms.ModelForm):

    class Meta:

        model = Work

        fields = '__all__'

        widgets = dict(
            anthologies=Select2MultipleWidget,
            author=Select2Widget,
            parent=Select2Widget,
        )
