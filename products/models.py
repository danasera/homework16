from pyexpat import model

from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=100,
                             primary_key=True)
    description = models.CharField(max_length=150)
    price = models.IntegerField()


    def __str__(self):
        return self.title