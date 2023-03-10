from django import forms
from AppColegio.models import Estudiante, Profesor

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

