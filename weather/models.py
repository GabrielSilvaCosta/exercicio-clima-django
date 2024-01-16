# Arquivo: weather/models.py

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=60)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    def slugify(self):
        lower_name = self.name.replace(" ", "-").lower()
        return lower_name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(City, self).save(*args, **kwargs)


class DailyWeather(models.Model):
    CHOICES = [
        ("Ensolarado", "Ensolarado"),
        ("Nublado", "Nublado"),
        ("Chuvoso", "Chuvoso"),
        ("Parcialmente nublado", "Parcialmente nublado"),
        ("Neve", "Neve"),
        ("Granizo", "Granizo"),
    ]

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField(unique_for_date="city")
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    brief_description = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return f"{self.date.strftime('%d/%m/%Y')} - {self.brief_description}"
