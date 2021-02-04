from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.

class EstadoSolicitud(models.Model):
    estado = models.CharField(max_length=25)
    def __str__(self):
        return self.estado
    class Meta:
        verbose_name = "EstadoSolicitud"
        verbose_name_plural = "Estado Solicitudes"

class Aplicacion(models.Model):
    nombre = models.CharField(max_length=100)
    activa = models.BooleanField()
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Aplicacion"
        verbose_name_plural = "Aplicaciones"

class UsuarioAplicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.PROTECT)
    activa = models.BooleanField()

class SolicitudUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    login = models.CharField(max_length=100)
    clave = models.CharField(max_length=50)
    quien_solicita = models.ForeignKey(User, on_delete=models.PROTECT)
    estado_solicitud = models.ForeignKey(EstadoSolicitud, on_delete=models.PROTECT)
    fecha_solcitud = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.login
    class Meta:
        verbose_name_plural = "Solicitud de usuarios"





    


