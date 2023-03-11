from django import forms
from AppColegio.models import Estudiante, Profesor, Curso

#Formulario para estudiante
class EstudForm(forms.ModelForm):
    class Meta():
        model = Estudiante
        fields = '__all__'

#Formulario para Profesor
class ProfeForm(forms.ModelForm):
    class Meta():
        model = Profesor
        fields = '__all__'


#formulario para Curso
class CurForm(forms.ModelForm):
    class Meta():
        model = Curso
        fields = ("nombre", "camada")

