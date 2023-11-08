# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world_text, name='hello'),
    path('book_programm_lang/', views.book_view, name='book'),
]