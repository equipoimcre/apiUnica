from django.contrib import admin
from usuarios.models import EstadoSolicitud, Aplicacion,SolicitudUsuario,UsuarioAplicacion



# Register your models here.

admin.site.register(EstadoSolicitud)
admin.site.register(Aplicacion)
admin.site.register(SolicitudUsuario)
admin.site.register(UsuarioAplicacion)
