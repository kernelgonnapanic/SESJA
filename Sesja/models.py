from django.db import models

# Create your models here.

class Modelik(models.Model):
    slowa = models.CharField(max_length=150)
    data = models.DateTimeField('data_nasza')
    liczba = models.IntegerField(default=21)

