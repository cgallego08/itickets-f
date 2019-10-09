from django.db import models

from apps.asistentes.models import Attendee

from apps.tickets.models import Ticket

from apps.escenarios.models import Escenario, Ciudad


# Create your models here.

class Evento(models.Model):
    nombre_evento = models.CharField(max_length=250)
    descripcion_evento = models.TextField(blank=True, null=True)
    nombre_escenario = models.ForeignKey(Escenario, null= True, blank=True, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, null= True, blank=True, on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket, blank=True)
    asitentes = models.ManyToManyField(Attendee, blank=True)
    direccion = models.CharField(max_length=250)
    fecha_inicio_evento = models.DateTimeField(null=True, blank=True)
    fecha_Fin_evento = models.DateTimeField(null=True, blank=True)
    imagen = models.ImageField(upload_to='uploads')


    def __str__(self):
        return '{}'.format(self.nombre_evento)

