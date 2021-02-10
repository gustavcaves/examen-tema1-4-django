from django.db import models

# Create your models here.

class Peliculas(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre de la película")
    description = models.CharField(max_length=1000, verbose_name="Descripción")
    year = models.DateField(verbose_name="Año de lanzamiento")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación en db")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de última actualización en db")

    class Meta:
        verbose_name="Película"
        verbose_name="Películas"
        ordering = ['title','year']

    def __str__(self):
        return self.title

class programacionSala(models.Model):
    date = models.DateField(verbose_name="Fecha de presentación de película")
    hour = models.TimeField(verbose_name="Hora de presentacion de película")
    movie = models.ForeignKey(Peliculas, on_delete=models.PROTECT, verbose_name="Película")

    def __str__(self):
        return self.date