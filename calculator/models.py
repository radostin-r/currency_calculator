from django.db import models


# Create your models here.
class ExchangeRate(models.Model):

    currency_pair = models.CharField(max_length=10, primary_key=True)
    exchange_rate = models.FloatField()
