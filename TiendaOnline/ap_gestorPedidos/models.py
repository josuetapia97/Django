from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    tfon = models.CharField(max_length=10, verbose_name="telefono")

    def __str__(self):
        return "nombre de persona {} direccion {} email {} telefono {}".format(self.nombre,self.direccion,self.email,self.tfon)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return "nombre {} seccion {} precio {}".format(self.nombre,self.seccion,self.precio)
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
