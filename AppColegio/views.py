from AppColegio.forms import EstudForm
from django.shortcuts import render
from AppColegio.models import Estudiante

# Create your views here.


def index(request):
    return render(request, "AppColegio/index.html")


def mostrar_estudiante(request):
    contex = {
        "form": EstudForm(),
        "posts": Estudiante.objects.all(),
    }
    return render(request, "AppColegio/carga_estudiante.html", contex)




def agregar_estudiante(request):
    form_post = EstudForm(request.POST)
    form_post.save()  # Construyo objeto tipo EstudForm con los datos cargados por el usuario
    context = {
        "form": EstudForm(),
        "estudiantes": Estudiante.objects.all(),
    }
    return render(request, "AppColegio/carga_estudiante.html", context)
