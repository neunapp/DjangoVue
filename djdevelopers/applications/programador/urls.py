from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        '', 
        views.HomeView.as_view(),
        name='index',
    ),
    path(
        'add/', 
        views.ProgramadorCreateView.as_view(),
        name='add',
    ),
    path(
        'add-programador/', 
        views.AddProgramadorView.as_view(),
        name='add-programador',
    ),


    # urls de los servicios
    path(
        'api/lenguaje/search/', 
        views.LenguajeListApiView.as_view(),
        name='lenguaje-buscar',
    ),
    path(
        'api/programador/register/', 
        views.RegistrarProgramador.as_view(),
        name='programador-register',
    ),
]