from django.http import HttpResponse
from django.shortcuts import render
from . import models


def hello_world_text(request):
    return HttpResponse("Добро пожаловать на пробный сайт!\n"
                        "Не обещаю что он самый лучший но в топ 10 точно попадет))")


def book_view(request):
    book = models.BookProgrammlang.objects.all()
    return render(request, 'book.html', {'book': book})
