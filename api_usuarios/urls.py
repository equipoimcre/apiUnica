"""api_usuarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import api_usuarios.views # carga las vista de la pagina web base
import usuarios.views


urlpatterns = [
    path('', api_usuarios.views.index, name='index'), # Pagina de inicio 
    path('usuarios/', usuarios.views.home, name = 'usuarios'),
    path('usuarios/solicitar_usuario/', usuarios.views.solicitar_usuario, name = 'solicitar_usuario'), 
    path('aplicaciones/', usuarios.views.aplicaciones, name = 'aplicaciones'), 
    path('aplicaciones/alta_aplicacion/', usuarios.views.alta_aplicacion, name = 'alta_aplicacion'), 
    path('admin/', admin.site.urls), # con /admin nos abre la pagina de administracion
]
