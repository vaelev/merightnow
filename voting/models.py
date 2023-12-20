from django.db import models

class Feeling(models.Model):
    emoji = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)