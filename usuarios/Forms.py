from django import forms
from usuarios.models import SolicitudUsuario, Aplicacion

class SolicitarUsuarioForm(forms.ModelForm):
	class Meta:
		model = SolicitudUsuario
		fields = "__all__"

class AplicacionForm(forms.ModelForm):
	class Meta:
		model = Aplicacion
		fields = "__all__"
