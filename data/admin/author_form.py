

from django import forms
from django_select2.forms import Select2Widget, Select2MultipleWidget

from data.models import Author


class AuthorForm(forms.ModelForm):

    class Meta:

        model = Author

        fields = '__all__'

        widgets = dict(
            country=Select2Widget,
            genre=Select2MultipleWidget,
            race=Select2MultipleWidget,
        )
