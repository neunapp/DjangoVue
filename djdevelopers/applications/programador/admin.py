from django.contrib import admin

# Register your models here.
from .models import Lenguaje, Programador

admin.site.register(Lenguaje)
admin.site.register(Programador)
