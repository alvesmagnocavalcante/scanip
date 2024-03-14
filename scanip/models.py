from django.db import models

class Dispositivo(models.Model):
    ip = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
