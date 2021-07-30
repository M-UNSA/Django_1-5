"""listaContactos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from inicio.views import myHomeView, anotherView
from personas.views import (
    personaTestView,
    personaCreateView, 
    searchForHelp, 
    searchPersona, 
    personasAnotherCreateView, 
    personaShowObject,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myHomeView, name='Página de Inicio'),
    path('otro', anotherView, name='otro'),
    path('persona', personaTestView, name='persona'),
    path('agregar', personaCreateView, name='createPersona'),
    path('ayuda', searchForHelp, name='ayuda'),
    path('buscar', searchPersona, name='buscar'),
    path('add', personasAnotherCreateView, name='OtroAgregarPersona'),
    path('persona/<int:myID>', personaShowObject, name = 'browsing')
]
