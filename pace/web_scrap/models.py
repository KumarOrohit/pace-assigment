from django.db import models

# Create your models here.


class WebScrapData(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    h1 = models.CharField(max_length=100)
    h24 = models.CharField(max_length=100)
    d7 = models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100)
    volume_24h = models.CharField(max_length=100)
    circulating_supply = models.CharField(max_length=100)