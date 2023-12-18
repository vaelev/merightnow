from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Feeling(models.Model):
    emoji = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.emoji
