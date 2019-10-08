from django.db import models
from django.utils import timezone


# Create your models here.

class Departamento(models.Model):
    id_departamento = models.IntegerField(primary_key=True)
    departamento = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.departamento, self.id_departamento)

class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    ciudad = models.CharField(max_length=250)
    estado = models.IntegerField()
    departamento_id = models.ForeignKey(Departamento, null= True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.ciudad, self.departamento_id)

class Escenario(models.Model):
    nombre_escenario = models.CharField(max_length=250)
    capacidad_escenario = models.CharField(max_length=250)
    direccion_escenario = models.CharField(max_length=250)
    departamento_escenario = models.ForeignKey(Departamento, null= True, blank=True, on_delete=models.CASCADE)
    ciudad_escenario = models.ForeignKey(Ciudad, null= True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_escenario)