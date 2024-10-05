from django.db import models

# Create your models here.


class Vehiculo(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20)
    precio = models.IntegerField()
    # auto_now_add=True la fecha queda fija para siempre
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ('visualizar_catalogo', 'Puede visualizar el catálogo de vehículos'),
            ("add_vehiculomodel", "Puede agregar vehículos"),
        ]

    def __str__(self):
        return f'{self.marca} {self.modelo}'
