# mi_aplicacion/forms.py
from django import forms
from .models import Persona, Producto, Pedido

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class PersonaSearchForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False, label='Nombre')


