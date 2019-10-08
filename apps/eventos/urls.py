from django.urls import path
from apps.eventos.views import index, evento_list, evento_view

urlpatterns = [
    path('', index, name='eventos'),
    path('nuevo', evento_view, name='eventos_crear'),
    path('listar', evento_list, name='eventos_listar'),

]