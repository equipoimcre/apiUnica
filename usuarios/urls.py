from django.urls import path
from usuarios import views

urlpatterns = [
    path("", views.home, name="home"), # Si no se pone nada lanza la funcion views.home
    path("crear_usuario", views.crear_usuario, name="crear_usuario"), # Si no se pone nada lanza la funcion views.home
]
