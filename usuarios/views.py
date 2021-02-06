from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import SolicitudUsuario, Aplicacion, EstadoSolicitud, UsuarioAplicacion
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
    print(request.user)
    instancia = SolicitudUsuario.objects.get(id=id)
    form = SolicitarUsuarioForm(instance=instancia)
    usuarios = SolicitudUsuario.objects.filter(id=id)
    if request.method == "POST":
        form = SolicitarUsuarioForm(request.POST or None, instance=instancia)
        if form.is_valid():
            #instancia = form.save(commit=False)
            #instancia.save()
            return redirect('/')
    # aqui falta el engache con la api
    ddbbs = ['a','b',1,2,3,4,5,6,7,8]
    perfiles_pentajo = [1,2,3,4,5,6,7,8]
    forms_odk = [1,2,3,4,5,6,7,8]
    return render(request, "asignar_permisos_2.html", {
        'form' : form,
        'usuarios' : usuarios,
        'ddbbs' : ddbbs,
        'perfiles_pentajo' : perfiles_pentajo,
        'forms_odk' : forms_odk
        })

def resultado(request):
    form = RespuestaForm(request.POST)
    nombre = request.POST.get('nombre',False)
    if request.method == "POST":
        if form.is_valid():
            #instancia = form.save(commit=False)
            #instancia.save()
            return HttpResponse("en pruebas dentro")
    # aqui falta el engache con la api
    print(nombre)
    print(form)
    return HttpResponse("en pruebas fuera" )




