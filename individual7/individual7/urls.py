"""
URL configuration for individual7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app7.views import home, LoginUsuario, perfilp, registro, detalle_tarea, crear_tarea

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', LoginUsuario.as_view(), name='LoginUsuario'),
    path('perfil/', perfilp, name='perfilp'),
    path('registrate/', registro, name='registro'),
    path('tarea/', detalle_tarea, name='detalle_tarea'),
    path('crear-tarea/', crear_tarea, name='crear_tarea')
]
