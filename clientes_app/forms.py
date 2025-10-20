from django import forms
from .models import Cliente, Producto, Compra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class BuscarClienteForm(forms.Form):
    nombre = forms.CharField(label='Buscar cliente por nombre', max_length=100)
