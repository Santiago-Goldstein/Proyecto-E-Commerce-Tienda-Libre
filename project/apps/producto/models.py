from django.db import models
from django.utils import timezone


class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "categoría de productos"
        verbose_name_plural = "categorías de productos"
