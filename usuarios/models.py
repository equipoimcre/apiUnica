from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from fernet_fields import EncryptedTextField, EncryptedCharField


# Create your models here.

ESTADOS = [
    ('1', 'Socitado'),
    ('2', 'Aceptado'),
    ('3', 'Rechazado'),
    ('4', 'Tramitado'),
]

class SolicitudUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    login = models.CharField(max_length=100)
    clave = EncryptedCharField(max_length=100)
    estado_solicitud = models.CharField(max_length=1, choices=ESTADOS)
    fecha_solcitud = models.DateTimeField(auto_now_add=True)
    user_mysql = models.BooleanField()
    ddbb_mysql = models.TextField(null=True, blank=True)
    user_pentajo = models.BooleanField()
    roll_pentajo = models.TextField(null=True, blank=True)
    user_odk = models.BooleanField()
    form_odk = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.login
    class Meta:
        verbose_name_plural = "Solicitud de usuarios" # El nombre que sale la web de admin





    


