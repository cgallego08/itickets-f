from django import forms
from apps.eventos.models import Evento

class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento

        fields = [
            'nombre_evento',
            'descripcion_evento',
            'nombre_escenario',
            'ciudad',
            'tickets',
            'asitentes',
            'direccion',
            'fecha_inicio_evento',
            'fecha_Fin_evento',
        ]

        lables = {
            'nombre_evento': 'Nombre Evento',
            'descripcion_evento': 'Descripcion Evento',
            'nombre_escenario': 'Nombre Escenario',
            'ciudad': 'Ciudad',
            'tickets': 'Tickets',
            'asitentes': 'Asistentes',
            'direccion': 'Direccion',
            'fecha_inicio_evento': 'Fecha Inicio Evento',
            'fecha_Fin_evento': 'Fecha Fin Evento',
        }
        widgets = {
            'nombre_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'tickets': forms.CheckboxSelectMultiple(),
            'asistentes': forms.CheckboxSelectMultiple(),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_Fin_evento': forms.TextInput(attrs={'class': 'form-control'}),

        }






