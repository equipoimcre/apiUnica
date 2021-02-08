from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import SolicitudUsuario
from usuarios.forms import SolicitarUsuarioForm, RespuestaForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def usuarios(request):
    usuarios = SolicitudUsuario.objects.all()
    return render(request, 'home.html', {
        'usuarios' : usuarios
    })

def usuarios_solicitados(request):
    usuarios = SolicitudUsuario.objects.filter(estado_solicitud=1)
    text = 'Usuarios pendiendes de aprobar'
    return render(request, 'home.html', {
        'usuarios' : usuarios, 'text': text
    })

def usuarios_aprobados(request):
    usuarios = SolicitudUsuario.objects.filter(estado_solicitud=2)
    text = 'Usuarios pendiendes de tramitar '
    return render(request, 'usuarios_aprobados.html', {
        'usuarios' : usuarios, 'text': text
    })


def usuarios_tramitados(request):
    usuarios = SolicitudUsuario.objects.filter(estado_solicitud=4)
    text = 'Usuarios Tramitados'
    return render(request, 'home.html', {
        'usuarios' : usuarios, 'text': text
    })

def solicitar_usuario(request):
    form = SolicitarUsuarioForm()
    if request.method == "POST":
        form = SolicitarUsuarioForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/')
    # aqui falta el engache con la api
    text = 'Solicitud de usuario'
    return render(request, "solicitar_usuario.html",  {'form': form, 'text': text})

def editar_usuario(request, id):
    instancia = SolicitudUsuario.objects.get(id=id)
    form = SolicitarUsuarioForm(instance=instancia)
    if request.method == "POST":
        form = SolicitarUsuarioForm(request.POST or None, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/')
    text = 'Edicion de usuario'
    return render(request, "solicitar_usuario.html", {'form': form, 'text': text})


def asignar_permisos(request, id):
    usuarios = SolicitudUsuario.objects.filter(id=id)
    ddbbs = ['a','b',1,2,3,4,5,6,7,8]
    perfiles_pentajo = [1,2,3,4,5,6,7,8]
    forms_odk = [1,2,3,4,5,6,7,8]
    return render(request, "asignar_permisos.html", {
        'usuarios' : usuarios,
        'ddbbs' : ddbbs,
        'perfiles_pentajo' : perfiles_pentajo,
        'forms_odk' : forms_odk
        })

def resultado(request):
    
    #guardo los datos del form
    nombre = request.POST.get('nombre',False)
    correo = request.POST.get('correo',False)
    login = request.POST.get('login',False)
    clave = request.POST.get('clave',False)
    user_mysql = request.POST.get('user_mysql',False)
    ddbb_mysql = request.POST.getlist("ddbb_mysql")
    user_pentajo = request.POST.get('user_pentajo',False)
    roll_pentajo = request.POST.getlist("roll_pentajo")
    user_odk = request.POST.get('user_odk',False)
    form_odk = request.POST.getlist("form_odk")
    usuario = SolicitudUsuario.objects.get(nombre=nombre)
    print(usuario.estado_solicitud)
    if request.method == "POST":
        try:
            # cambiar el estado a procesado
            usuario.estado_solicitud = 4
            print(usuario.estado_solicitud)
            usuario.save() 
            # aqui falta el engache con la api
            return render(request, "tramitado_ok.html", {'usuario': usuario.nombre})
        except Exception as e:
            return render(request, "tramitado_mal.html", {'error': e})

    return HttpResponse("en pruebas fuera" )

def buscar_usuario(request):
    usuarios = SolicitudUsuario.objects.filter(estado_solicitud=4)
    return render(request, 'buscar_usuario.html', {
        'usuarios' : usuarios
    })

def editar_permisos(request):
    username = request.POST.get('login',False)
    if request.method == "POST":
        # perdir los todos los datos
        ddbbs = ['a','b',1,2,3,4,5,6,7,8]
        perfiles_pentajo = [1,2,3,4,5,6,7,8]
        forms_odk = [1,2,3,4,5,6,7,8]
        # pedir los datos del usuario
        username_ddbbs = [1,2,3]
        username_perfiles_pentajo = [1,2,3]
        username_forms_odk = [1,2,3]
        return render(request, "editar_permisos.html", {
        'username' : username,
        'ddbbs' : ddbbs,
        'perfiles_pentajo' : perfiles_pentajo,
        'forms_odk' : forms_odk,
        'username_ddbbs' : username_ddbbs,
        'username_perfiles_pentajo' : username_perfiles_pentajo,
        'username_forms_odk' : username_forms_odk
        })
   
    return HttpResponse("en pruebas editar_usario 1.2 " + str(a)  )

def editar_permisos2(request, login):
    username = login
    # perdir los todos los datos
    ddbbs = ['a','b',1,2,3,4,5,6,7,8]
    perfiles_pentajo = [1,2,3,4,5,6,7,8]
    forms_odk = [1,2,3,4,5,6,7,8]
    # pedir los datos del usuario
    username_ddbbs = [1,2,3]
    username_perfiles_pentajo = [1,2,3]
    username_forms_odk = [1,2,3]
    return render(request, "editar_permisos.html", {
        'username' : username,
        'ddbbs' : ddbbs,
        'perfiles_pentajo' : perfiles_pentajo,
        'forms_odk' : forms_odk,
        'username_ddbbs' : username_ddbbs,
        'username_perfiles_pentajo' : username_perfiles_pentajo,
        'username_forms_odk' : username_forms_odk
        })





