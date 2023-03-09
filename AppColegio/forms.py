from django import forms
from AppColegio.models import Estudiante


class EstudForm(forms.ModelForm):
    class Meta():
        model = Estudiante
        fields = '__all__'
