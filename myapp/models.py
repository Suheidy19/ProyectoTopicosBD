from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=50, verbose_name='Nombre')
    Quantity = models.IntegerField(verbose_name='Cantidad', )
    Price = models.DecimalField(verbose_name='Precio', max_digits=5, decimal_places=2, default=0.00)
    Expiration = models.DateField(verbose_name='Fecha de Caducidad')

    def __str__(self):
        return "{0} {1} {2}".format(self.Name, self.Price, self.Expiration)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


class Service(models.Model):
    Name = models.CharField(max_length=50, verbose_name="Nombre del servicio")
    Description = models.CharField(max_length=500, verbose_name="Descripción")

    def __str__(self):
        return "{0}".format(self.Name)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
