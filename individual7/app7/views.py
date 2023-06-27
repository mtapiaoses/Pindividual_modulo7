from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from app7.forms import Login, Registro
from app7.models import Perfil
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    context = {'clave':'valor'}
    return render(request, 'home.html', context)

# def login(request):
#     if request.method == 'POST':
#         formulario = Login(request.POST)
#         print("estoy en el login, antes de validar")

#         if formulario.is_valid():
#             username = formulario.cleaned_data['usuario']
#             password = formulario.cleaned_data['clave']

#             user = authenticate(username=username, password=password)
#             print(user)
            
#             if user is not None:
#                 login(request, user)
#                 return render(request, 'perfil.html')
#                 # return redirect ('/perfil/')
            
#             return redirect('/')
#     else:
#         formulario = Login()
#         return render(request, 'login.html' , {'formulario':formulario})

class LoginUsuario(TemplateView):
    def get(self, request, *args, **kwargs):
        formulario = Login()
        context = {'formulario':formulario}
        return render(request, 'login.html', context)
    
    def post(self, request, *args, **kwargs):
        print(request.POST['usuario'])
        print(request.POST['clave'])
        formulario = Login(request.POST)
        if formulario.is_valid():
            print("pase el login")
            username = formulario.cleaned_data['usuario']
            password = formulario.cleaned_data['clave']
            user = authenticate(username=username, password=password)
            print(user)

            if user is not None:
                  login(request, user)
                  print("a apunto de ir al perfil")
#                 return render(request, 'perfil.html')
                  return redirect ('/perfil/')
            print("a apunto de salir al perfil")
        return redirect('/')



def perfilp(request):
    print("entre al perfil")
    perfil = Perfil.objects.get(user_id=request.user.id)
    print("dsps del perfil")
    context = {'perfil':perfil}
    return render(request, 'perfil.html',context)

def registro(request):
    if request.method == 'POST':
        formulario = Registro(request.POST)

        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data['nombre_usuario']
            nombre = formulario.cleaned_data['nombre']
            apellido = formulario.cleaned_data['apellido']
            email = formulario.cleaned_data['email']
            clave = formulario.cleaned_data['clave']

            usuario = User(
                username=nombre_usuario,
                first_name=nombre,
                last_name=apellido,
                email=email)
            usuario.password = make_password(clave)
            usuario.save()

        return redirect('/login/')
    
    else:
        formulario = Registro()
        context = {'formulario':formulario}
        return render(request, 'registro.html', context)