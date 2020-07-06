#thry party apps
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import (
    ListView,
    CreateView,
    TemplateView
)
#
from .models import Programador, Lenguaje
#
from .forms import ProgramadorForm
#
from .serializers import (
    LenguajeSerializer,
    ProgramadorSerializer
)


class HomeView(ListView):
    template_name = "programador/index.html"
    context_object_name = 'programadores'
    model = Programador


class ProgramadorCreateView(CreateView):
  
    template_name = "programador/add.html"
    form_class = ProgramadorForm
    success_url = reverse_lazy('persona_app:index')


class AddProgramadorView(TemplateView):
    template_name = "programador/add_programador.html"



"""  aqui empiezan los servicios """

class LenguajeListApiView(ListAPIView):
    serializer_class = LenguajeSerializer
    
    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')

        return Lenguaje.objects.filter(
            languages__icontains=kword
        )


class RegistrarProgramador(CreateAPIView):
    serializer_class = ProgramadorSerializer