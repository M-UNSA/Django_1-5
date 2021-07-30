from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm, RawPersonaForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

# Create your views here.
class PersonaListView(ListView) :
    model = Persona
    queryset = Persona.objects.filter(edad__lte='29')

class PersonaDetailView(DetailView) :
    model = Persona

class PersonaCreateView(CreateView) :
    model = Persona
    fields = [
        'nombre',
        'apellidos',
        'edad',
        'donador',
    ]

def personaTestView(request) :
    obj = Persona.objects.get(id = 1)
    context = {
        'objeto' : obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView(request) :
    initialValues = {
        'nombre' : 'Sin Nombre'
    }
    form = PersonaForm(request.POST or None, initial = initialValues)
    if form.is_valid():
        form.save()
        form = PersonaForm()

    context = {
        'form' : form
    }
    return render(request, 'personas/personasCreate.html', context)

def searchPersona(request) :
    print('GET: ', request.GET)
    print('POST: ', request.POST)
    context = {}
    return render(request, 'personas/personaBuscar.html', context)

def searchForHelp(request) :
    return render(request,'personas/search.html', {})

def personasAnotherCreateView(request) :
    form = RawPersonaForm() #request.GET
    if request.method == "POST" :
        form = RawPersonaForm(request.POST)
        if form.is_valid() :
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form' : form,
    }
    return render(request, 'personas/personasCreate.html', context)

def personaShowObject(request, myID) :
    obj = get_object_or_404(Persona, id = myID)
    context = {
        'objeto' : obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personaDeleteView(request, myID) :
    obj = get_object_or_404(Persona, id = myID)
    if request.method == 'POST' :
        print("lo borro")
        obj.delete()
        return redirect('/personas')
    context = {
        'objeto' : obj,
    }
    return render(request, 'personas/personaBorrar.html', context)

def personasListView(request) :
    queryset = Persona.objects.all()
    context = {
        'objectList' : queryset,
    }
    return render(request, 'personas/personasLista.html', context)