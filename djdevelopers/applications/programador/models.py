from django.db import models

from django.db import models


class Lenguaje(models.Model):
    
    languages = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Lenguajes de Programacion'
        verbose_name_plural = 'Lenguajes de Programacion'

    def __str__(self):
        return str(self.id) + ' ' + self.languages


class Programador(models.Model):

    full_name = models.CharField('Nombre', max_length=60)
    ocupation = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    languages = models.ManyToManyField(Lenguaje)

    class Meta:
        verbose_name='Programador'
        verbose_name_plural='Programadores'
        ordering=['full_name']

    def __str__(self):
        return str(self.id) + ' ' + self.full_name
