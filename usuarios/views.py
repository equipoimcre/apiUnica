from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import SolicitudUsuario, Aplicacion, EstadoSolicitud, UsuarioAplicacion
# Create your views here.


def home(request):
    usuarios = SolicitudUsuario.objects.filter(estado_solicitud=1)
    return render(request, 'home.html', {
        'usuarios' : usuarios
    })

def aplicaciones(request):

    aplicaciones = Aplicacion.objects.all()
    return render(request, 'aplicaciones.html', {
        'aplicaciones' : aplicaciones
    })

def solicitar_usuario(request):
    usuario = SolicitudUsuario(
    )
    return HttpResponse("Usuario Creado")

