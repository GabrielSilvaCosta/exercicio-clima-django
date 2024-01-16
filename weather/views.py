# Arquivo: weather/views.py

from django.shortcuts import render
from weather.models import City, DailyWeather


def index(request):
    cities = {"cities": City.objects.all()}
    return render(request, "home.html", cities)


def city_weather(request, city):
    city_name = city.replace("-", " ").title()

    queried_city = City.objects.get(name=city_name)
    weathers = DailyWeather.objects.filter(city=queried_city)

    context = {"city": queried_city, "weathers": weathers}
    return render(request, "city_weather.html", context)
