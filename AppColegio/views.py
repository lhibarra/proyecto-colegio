from AppColegio.forms import EstudForm
from django.shortcuts import render
from AppColegio.models import Estudiante

# Create your views here.


def index(request):
    return render(request, "AppColegio/index.html")


def mostrar_estudiante(request):
    contex = {
        "form": EstudForm(),
        "estudiantes": Estudiante.objects.all(),
    }
    return render(request, "AppColegio/carga_estudiante.html", contex)


def agregar_estudiante(request):
    form_post = EstudForm(request.POST) # Construyo objeto tipo EstudForm con los datos cargados por el usuario
    form_post.save()  
    context = {
        "form": EstudForm(),
        "estudiantes": Estudiante.objects.all(),
    }
    return render(request, "AppColegio/carga_estudiante.html", context)


def buscar_estudiante(request):
    criterio = request.GET.get("criterio")
    context = {
        "estudiantes": Estudiante.objects.filter(nombre__icontains=criterio).all(),
    }
    return render(request, "AppColegio/carga_estudiante.html", context)
