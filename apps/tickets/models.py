from django.db import models

# Create your models here.

class Ticket(models.Model):
    nombre_ticket = models.CharField(max_length=250)
    precio_ticket = models.DecimalField(max_digits=10, decimal_places=3)
    cantidad_ticket = models.IntegerField()
    descripcion_ticket = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.nombre_ticket)