from django import forms
from usuarios.models import SolicitudUsuario, Aplicacion

DEMO_CHOICES =( 
    ("1", "Naveen"), 
    ("2", "Pranav"), 
    ("3", "Isha"), 
    ("4", "Saloni"), 
)


class SolicitarUsuarioForm(forms.ModelForm):
	class Meta:
		model = SolicitudUsuario
		fields = [ 'nombre', 
    		'correo', 
    		'login', 
    		'clave', 
    		'estado_solicitud',  
    		'user_mysql',
    		'ddbb_mysql',
    		'user_pentajo', 
    		'roll_pentajo',
    		'user_odk', 
    		'form_odk', 

		]
		label = {
		 	'nombre':'Nombre del soliciante', 
    		'correo':'Correo electronico del solicitante', 
    		'login':'Nombre del usuario', 
    		'clave':'Contraseña', 
    		'estado_solicitud':'Estado de la solicitud',  
    		'user_mysql':'Generar usuario de Mysql',
    		'ddbb_mysql':'DDBB a las que tiene acceso',
    		'user_pentajo':'Generar usuario de Pentajo', 
    		'roll_pentajo':'Roles de Pentajo',
    		'user_odk':'Generar usuario de ODK', 
    		'form_odk':'Formularios a los que tiene acceso', 

		}
		widgets = {
		 	'nombre':forms.TextInput(),
    		'correo':forms.TextInput(),
    		'login':forms.TextInput(),
    		'clave':forms.PasswordInput(render_value=True),
    		'estado_solicitud':forms.Select(),  
    		'user_mysql':forms.CheckboxInput(),
    		'ddbb_mysql':forms.TextInput(attrs={'required': False}),
    		'user_pentajo':forms.CheckboxInput(),
    		'roll_pentajo':forms.TextInput(attrs={'required': False}),
    		'user_odk':forms.CheckboxInput(),
    		'form_odk':forms.TextInput(attrs={'required': False}),

		}

class RespuestaForm(forms.Form):
	class Meta:
		fields = [ 'nombre', 
    		'correo', 
    		'login', 
    		'clave', 
    		'estado_solicitud',  
    		'user_mysql',
    		'ddbb_mysql',
    		'user_pentajo', 
    		'roll_pentajo',
    		'user_odk', 
    		'form_odk', 

		]
		label = {
		 	'nombre':'Nombre del soliciante', 
    		'correo':'Correo electronico del solicitante', 
    		'login':'Nombre del usuario', 
    		'clave':'Contraseña', 
    		'estado_solicitud':'Estado de la solicitud',  
    		'user_mysql':'Generar usuario de Mysql',
    		'ddbb_mysql':'DDBB a las que tiene acceso',
    		'user_pentajo':'Generar usuario de Pentajo', 
    		'roll_pentajo':'Roles de Pentajo',
    		'user_odk':'Generar usuario de ODK', 
    		'form_odk':'Formularios a los que tiene acceso', 

		}
		widgets = {
		 	'nombre':forms.TextInput(),
    		'correo':forms.TextInput(),
    		'login':forms.TextInput(),
    		'clave':forms.PasswordInput(render_value=True),
    		'estado_solicitud':forms.Select(),  
    		'user_mysql':forms.CheckboxInput(),
    		'ddbb_mysql':forms.MultipleChoiceField(),
    		'user_pentajo':forms.CheckboxInput(),
    		'roll_pentajo':forms.MultipleChoiceField(),
    		'user_odk':forms.CheckboxInput(),
    		'form_odk':forms.MultipleChoiceField(),

		}

