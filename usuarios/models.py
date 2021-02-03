from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EstadoSolicitud(models.Model):
    estado = models.CharField(max_length=25)

class Aplicacion(models.Model):
    nombre = models.CharField(max_length=100)
    activa = models.BooleanField()

class UsuarioAplicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.PROTECT)
    activa = models.BooleanField()

class SolicitudUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    login = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    quien_solicita = models.ForeignKey(User, on_delete=models.PROTECT)
    estado_solicitud = models.ForeignKey(EstadoSolicitud, on_delete=models.PROTECT)
    fecha_solcitud = models.DateTimeField(auto_now_add=True)




    


