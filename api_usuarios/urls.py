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
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls), # con /admin nos abre la pagina de administracion
    path('', api_usuarios.views.index, name='index'), # Pagina de inicio 
    path('login_page/', api_usuarios.views.login_page, name = 'login_page'),
    path('logout_page/', api_usuarios.views.logout_page, name = 'logout_page'),
    path('usuarios/', login_required(usuarios.views.home), name = 'usuarios'),
    path('usuarios_procesar/', login_required(usuarios.views.usuarios_procesar), name = 'usuarios_procesar'),
    path('usuarios/solicitar_usuario/', login_required(usuarios.views.solicitar_usuario), name = 'solicitar_usuario'),
    path('usuarios/editar_usuario/<int:id>', login_required(usuarios.views.editar_usuario), name = 'editar_usuario'),  
    path('aplicaciones/', login_required(usuarios.views.aplicaciones), name = 'aplicaciones'), 
    path('aplicaciones/alta_aplicacion/', login_required(usuarios.views.alta_aplicacion), name = 'alta_aplicacion'),     
]

