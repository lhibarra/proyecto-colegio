from AppColegio.models import Profesor, Estudiante, Curso

for _ in range(0, 10):
    Profesor(nombre="un profesor",
    apellido="Un apellido",
    email="mimail@gmail.com",
    profesion="prfesor de matematicas",
    ).save()

    Estudiante(nombre="un estudiante",
    apellido="apellido de estudiante",
    email="estud@gmail.com",
    ).save()

    Curso(nombre = "sexto año", 
    camada = 2000,
    ).save()
