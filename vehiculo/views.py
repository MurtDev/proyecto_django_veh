# vehiculo/views.py
from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import RegistroUsuarioForm

# def index(request):
#     return render(request, 'index.html', {})  # {} es un diccionario vacio


def index(request):
    return render(request, 'index.html')


@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add.html', {'form': form})


@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    # Clasificación de precios
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.categoria_precio = 'Bajo'
        elif 10000 < vehiculo.precio <= 30000:
            vehiculo.categoria_precio = 'Medio'
        else:
            vehiculo.categoria_precio = 'Alto'
    return render(request, 'vehiculo/listar.html', {'vehiculos': vehiculos})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Usuario o contraseña inválidos.")
        else:
            messages.error(request, "Usuario o contraseña inválidos.")
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"login_form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/')


# views.py


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'register_form': form})
