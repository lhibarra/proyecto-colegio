from AppColegio.forms import EstudForm, ProfeForm, CurForm
from django.shortcuts import render
from AppColegio.models import Estudiante, Profesor, Entregable, Curso


def index(request):
    return render(request, "AppColegio/index.html")

# Vistas para Model Estudiante


def mostrar_estudiante(request):
    contex = {
        "form": EstudForm(),
        "estudiantes": Estudiante.objects.all(),
    }
    return render(request, "AppColegio/carga_estudiante.html", contex)


def agregar_estudiante(request):
    # Construyo objeto tipo EstudForm con los datos cargados por el usuario
    form_post = EstudForm(request.POST)
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

# Vistas Para modelo Profesor


def mostrar_profesor(request):
    contex = {
        "form": ProfeForm(),
        "profesores": Profesor.objects.all(),
    }
    return render(request, "AppColegio/carga_profesor.html", contex)


def agregar_profesor(request):
    # Construyo objeto tipo ProfeForm con los datos cargados por el usuario
    form_post = ProfeForm(request.POST)
    form_post.save()
    context = {
        "form": ProfeForm(),
        "profesores": Profesor.objects.all(),
    }
    return render(request, "AppColegio/carga_profesor.html", context)


def buscar_profesor(request):
    criterio = request.GET.get("criterio")
    context = {
        "profesores": Profesor.objects.filter(profesion__icontains=criterio).all(),
    }
    return render(request, "AppColegio/carga_profesor.html", context)

# Vistas para Curso


def mostrar_curso(request):
    contex = {
        "form": CurForm(),
        "cursos": Curso.objects.all(),
    }
    return render(request, "AppColegio/carga_curso.html", contex)


def agregar_curso(request):
    # Construyo objeto tipo CursoForm con los datos cargados por el usuario
    form_post = CurForm(request.POST)
    form_post.save()
    context = {
        "form": CurForm(),
        "cursos": Curso.objects.all(),
    }
    return render(request, "AppColegio/carga_curso.html", context)


def buscar_camada(request):
    criterio = request.GET.get("criterio")
    context = {
        "cursos": Curso.objects.filter(camada=int(criterio)).all(),
    }
    return render(request, "AppColegio/carga_curso.html", context)
