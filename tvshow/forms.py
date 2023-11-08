from django import forms
from . import models


class TvshowForm(forms.ModelForm):
    class Meta:
        model = models.TvShow
        fields = "__all__"  # для отдельного поля "title name"


class FilmViewForm(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = '__all__'
