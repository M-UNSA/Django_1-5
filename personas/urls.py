from django.urls import path
from personas.views import (
    personaTestView,
    personaCreateView, 
    searchForHelp, 
    searchPersona, 
    personasAnotherCreateView, 
    personaShowObject,
    personaDeleteView,
    personasListView,
    )
from .views import (
    PersonaListView,
)

app_name = 'personas'
urlpatterns = [
    path('s', PersonaListView.as_view(), name = 'persona-list'),
    path('/test', personaTestView, name='persona'),
    path('/agregar', personaCreateView, name='createPersona'),
    path('/ayuda', searchForHelp, name='ayuda'),
    path('/buscar', searchPersona, name='buscar'),
    path('/add', personasAnotherCreateView, name='OtroAgregarPersona'),
    path('/<int:myID>/', personaShowObject, name = 'browsing'),
    path('/<int:myID>/borrar/', personaDeleteView, name = 'deleting'),
    #path('s', personasListView, name='listing'),
]