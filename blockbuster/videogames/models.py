from django.db import models

# Create your models here.
class Game (models.Model):
    name = models.CharField(max_length=600)
    rating = models.PositiveIntegerField(range(1,10))
    in_stock = models.BooleanField(True)