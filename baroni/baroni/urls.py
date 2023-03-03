"""baroni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from baroni.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.urls import path, include
from .views import index, about


urlpatterns = [
    #Ruta Panel Administrador
    path('admin/', admin.site.urls),

    #Ruta Generales
    path('', index, name='index'),
    path('about/', about, name='about'),   

    #Rutas de APIS
    path('obras/', include('obras.urls')),
    path('clientes/', include('clientes.urls')),
    path('equipo/', include('equipo.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT) #Para cargar archivos estaticos
