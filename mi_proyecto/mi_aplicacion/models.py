from django.db import models

# Create your models here.

# Modelo Persona
class Persona(models.Model):
    nombre = models.CharField(max_length=100)   # Texto de hasta 100 caracteres
    edad = models.IntegerField()               # Número entero

# Modelo Autor
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        default="Anónimo",
        verbose_name="Nombre completo"
    )
    nacionalidad = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="Origen desconocido",
        verbose_name="Nacionalidad"
    )
    fecha_nacimiento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de Nacimiento (YYYY-MM-DD)"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="¿Autor activo?"
    )

    def __str__(self):
        return self.nombre
