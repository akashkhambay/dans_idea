from django.db import models

# Create your models here.
class Game (models.Model):
    name = models.CharField(max_length=600)
    rating = models.PositiveIntegerField(range(1,10))
    in_stock = models.BooleanField(True)

    # this changes the name of the item in the admin console
    def __str__(self):
        return f'{self.name}'
    
