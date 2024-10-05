# vehiculo/forms.py

from django import forms
from .models import Vehiculo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VehiculoForm(forms.ModelForm):
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota')
    ]

    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga')
    ]

    marca = forms.ChoiceField(choices=MARCAS, initial='Ford', label='Marca')
    categoria = forms.ChoiceField(
        choices=CATEGORIAS, initial='Particular', label='Categoría')

    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria',
                  'serial_motor', 'categoria', 'precio']
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_carroceria': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
