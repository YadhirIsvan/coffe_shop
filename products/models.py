from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(max_length=300, verbose_name="Descripción")  # Cambié 'Description' a minúscula
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")  # Cambié 'Price' a minúscula
    available = models.BooleanField(default=True, verbose_name="Disponible")  # Cambié 'Available' a minúscula y true a booleano
    photo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name="Foto")  # Cambié 'Photo' a minúscula

    def __str__(self):  
        return self.name  # Corregí el retorno a 'name', ya que 'description' no existe.
