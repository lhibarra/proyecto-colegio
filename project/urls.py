"""project URL Configuration

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
from django.urls import path
from AppColegio.views import index, agregar_estudiante, mostrar_estudiante, buscar_estudiante, agregar_profesor, mostrar_profesor, buscar_profesor, mostrar_curso, agregar_curso, buscar_camada





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= "index"),
    # urls de estudiante
    path('estudiante', mostrar_estudiante, name="ver-estudiante"),
    path('estudiante/agregar', agregar_estudiante, name="agregar-estudiante"),
    path('estudiante/buscar', buscar_estudiante, name="buscar-estudiante"),
    #urls de profesor
    path('profesor', mostrar_profesor, name="ver-profesor"),
    path('profesor/agregar', agregar_profesor, name="agregar-profesor"),
    path('profesor/buscar', buscar_profesor, name="buscar-profesor"),
    #urls curso
    path('curso', mostrar_curso, name="ver-curso"),
    path('curso/agregar', agregar_curso, name="agregar-curso"),
    path('curso/buscar', buscar_camada, name="buscar-camada"),
    
    

]
