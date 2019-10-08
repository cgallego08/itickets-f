from django.db import models
from apps.tickets.models import Ticket

# Create your models here.

class Attendee(models.Model):
    nombre_asistente = models.CharField(max_length=250)
    apellido_asistente = models.CharField(max_length=250)
    correo = models.EmailField(blank=True, unique=True)
    ticket = models.ForeignKey(Ticket, null= True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.nombre_asistente, self.apellido_asistente)
