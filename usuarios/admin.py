from django.contrib import admin
from usuarios.models import SolicitudUsuario



# Register your models here.

admin.site.register(SolicitudUsuario)


admin.site.site_header = "Gesion de usuarios Equipo IM"
