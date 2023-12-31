from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import models, forms, parser


class FilmListView(ListView):
    model = models.FilmParser
    template_name = 'film_list_parse.html'

    def get_queryset(self):
        return models.FilmParser.objects.all()


class ParserFormView(FormView):
    template_name = 'start_parsing.html'
    form_class = forms.ParserForm
    success_url = '/film_list/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Данные взяты....')

        else:
            return super(ParserFormView).post(*args, **kwargs)
