from django import forms
from details.models import Movies
class movieform(forms.ModelForm):

    class Meta:

        model=Movies
        fields="__all__"