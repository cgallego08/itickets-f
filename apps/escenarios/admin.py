from django.contrib import admin
from apps.escenarios.models import Escenario, Departamento, Ciudad

# Register your models here.
admin.site.register(Escenario)
admin.site.register(Departamento)
admin.site.register(Ciudad)

