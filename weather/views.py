# Arquivo: weather/views.py

from django.shortcuts import render
from weather.models import City


def index(request):
    cities = {"cities": City.objects.all()}
    return render(request, "home.html", cities)
