from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from app7.forms import Login, Registro, Filtro, TareaForm
from app7.models import Perfil, Tareas, Estado, Categoria
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    context = {'clave':'valor'}
    return render(request, 'home.html', context)

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
        return redirect('/perfil/')



def perfilp(request):
    print("vista perfilp")
    perfil = Perfil.objects.get(user=request.user)
    tareas = perfil.tareas.all()

    form = Filtro(request.GET)
    if form.is_valid():
        estado = form.cleaned_data['estado']
        if estado:
            tareas = tareas.filter(estado__estado = estado)

    context = {'tareas': tareas,
               'form': form
               }
    return render(request, 'perfil.html', context)

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
    
def detalle_tarea(request,):
    #return render(request,"tarea.html")
    pass

# def crear_tarea(request):
#     if request.method == 'POST':
#         form = TareaForm(request.POST)
#         if form.is_valid():
        
#             print("estoy creando la tareas")
#             tarea = TareaForm(
#                  titulo=form.cleaned_data['titulo'],
#                  descripcion=form.cleaned_data['descripcion'],
#                  fecha_publicacion=form.cleaned_data['fecha_publicacion'],
#                  fecha_vencimiento=form.cleaned_data['fecha_vencimiento'],
#                  estado=form.cleaned_data['estado'],
#                  categoria=form.cleaned_data['categoria']
#              )
#             tarea.save()
#             print("estoy guardando la tareas")
#             return redirect('/perfil/')  # Redirecciona a la página de perfil después de crear la tarea
#     else:
#         form = TareaForm()
    
#     return render(request, 'edicion_tarea.html', {'form': form})


#from app7.models import Estado

# ...

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            titulo = form.cleaned_data['titulo']
            descripcion = form.cleaned_data['descripcion']
            fecha_publicacion = form.cleaned_data['fecha_publicacion']
            fecha_vencimiento = form.cleaned_data['fecha_vencimiento']
            estado_choice = form.cleaned_data['estado']
            categoria_choice = form.cleaned_data['categoria']
            categoria = Categoria.objects.get(nombre=categoria_choice)
            
            # Obtener la instancia del modelo Estado según el valor seleccionado
            estado = Estado.objects.get(estado=estado_choice)
            perfil = Perfil.objects.get(user_id=request.user.id)
            user = User.objects.get(id=request.user.id)
            print(f" CATEGORIA : {categoria.nombre}")
            
            tarea = Tareas(
                titulo=titulo,
                contenido=descripcion,
                fecha_publicacion=fecha_publicacion,
                fecha_vencimiento=fecha_vencimiento,
                estado=estado,
                categorias=categoria,
                autor=user
            )
            
            tarea.save()
            
            perfil.tareas.add(tarea)  
            print(type(perfil.tareas))
            perfil.save() 
    
       
             


            return redirect('/perfil/')
    else:
        form = TareaForm()
    
    return render(request, 'edicion_tarea.html', {'form': form})


