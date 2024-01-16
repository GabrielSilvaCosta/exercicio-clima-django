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
