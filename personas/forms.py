from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm) :
    class Meta :
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'donador',
        ]

class RawPersonaForm(forms.Form) :
    nombre = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'placeholder' : 'Sólo tu nombre, por favor',
                'id' : 'nombreID',
                'class' : 'special',
                'cols' : '10',
            }
        )
    )
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial = 20)
    donador = forms.BooleanField()