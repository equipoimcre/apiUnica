from django.urls import path
from usuarios import views

urlpatterns = [
    path("", views.home, name="home"),
]