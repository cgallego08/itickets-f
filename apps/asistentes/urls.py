from django.urls import path
from .views import asistentes

urlpatterns = [
    path('', asistentes, name='asistentes'),
]