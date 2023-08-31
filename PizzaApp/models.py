from django.db import models

# Create your models here.
class PizzaModel(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    description = models.TextField(max_length=70)