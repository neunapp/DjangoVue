from django import forms

from .models import Programador, Lenguaje
#


class ProgramadorForm(forms.ModelForm):
    """  formulario para seleccionar autores """

    languages = forms.ModelMultipleChoiceField(
        queryset=Lenguaje.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Programador
        fields = (
            'full_name',
            'ocupation',
            'age',
            'languages',
        )
        widgets = {
            'full_name': forms.TextInput(
                attrs = {
                    'placeholder': 'Nombres..',
                    'class': 'form-control',
                }
            ),
            'ocupation': forms.TextInput(
                attrs = {
                    'placeholder': 'Ocupacion..',
                    'class': 'form-control',
                }
            ),
            'age': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
        }