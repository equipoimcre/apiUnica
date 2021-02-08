from django.urls import path
from usuarios import views

urlpatterns = [
    path("", views.home, name="home"), # Si no se pone nada lanza la funcion views.home
]
