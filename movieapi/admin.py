from django.contrib import admin
from .models import Movie
from django.core import management
from django.shortcuts import redirect


# Register your models here.
admin.site.register(Movie)