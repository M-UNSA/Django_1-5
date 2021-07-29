from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    edad = models.DecimalField(max_digits=3,decimal_places=0)
    donador = models.BooleanField()