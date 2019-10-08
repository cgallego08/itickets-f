from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.eventos.models import Evento
from apps.eventos.forms import EventoForm
from apps.asistentes.models import Attendee
# Create your views here.

def index(request):
    return render(request, 'eventos/index.html')

def evento_view(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('evento:index')
    else:
            form = EventoForm()
    return render(request, 'eventos/crear_eventos.html', {'form':form})

def evento_list(request):
    evento = Evento.objects.all()
    listaAsistente = Attendee.objects.count()
    contexto = {'eventos':evento, 'listaAsistente':listaAsistente}
    return render(request, 'eventos/lista_eventos.html', contexto)