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
    PersonaDetailView,
    PersonaCreateView,
    PersonaUpdateView,
    PersonaDeleteView,
)

app_name = 'personas'
urlpatterns = [    
    path('/test', personaTestView, name='persona'),
    #path('/agregar', personaCreateView, name='createPersona'),
    path('/crear', PersonaCreateView.as_view(), name='persona-create'),
    path('/ayuda', searchForHelp, name='ayuda'),
    path('/buscar', searchPersona, name='buscar'),
    path('/add', personasAnotherCreateView, name='OtroAgregarPersona'),    
    #path('/<int:myID>/', personaShowObject, name = 'browsing'),
    path('/<int:pk>/', PersonaDetailView.as_view(), name = 'persona-detail'),
    path('/<int:pk>/actualizar', PersonaUpdateView.as_view(), name = 'persona-update'),
    #path('/<int:myID>/borrar/', personaDeleteView, name = 'deleting'),
    path('/<int:pk>/borrar', PersonaDeleteView.as_view(), name = 'persona-delete'),
    #path('s', personasListView, name='listing'),
    path('s', PersonaListView.as_view(), name = 'persona-list'),
]