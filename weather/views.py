# Arquivo: weather/views.py

from datetime import datetime
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


def weather_details(request, city, target):
    city_name = city.replace("-", " ").title()

    queried_city = City.objects.get(name=city_name)
    target_date = datetime.fromisoformat(target)
    weather = DailyWeather.objects.get(city=queried_city, date=target_date)

    context = {"city": queried_city, "weather": weather}
    return render(request, "weather_details.html", context)
