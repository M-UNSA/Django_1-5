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

    def clean_nombre(self, *args, **kwargs) :
        print('paso')
        name = self.cleaned_data.get('nombre')
        if name.istitle() :
            return name
        else :
            raise forms.ValidationError('La primera letra en mayúscula')

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