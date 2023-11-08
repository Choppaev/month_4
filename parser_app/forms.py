from django import forms
from . import parser, models


class ParserForm(forms.Form):
    MEDIA_CHOISES = (
        ('FILMIX', 'FILMIX'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOISES)

    class Meta:
        fields = [
            'media_type'
        ]

    def parser_data(self):
        if self.data['media_type'] == 'FILMIX':
            film_parser = parser.parser()
            for i in film_parser:
                models.FilmParser.objects.create(**i)