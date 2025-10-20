from django import forms
from .models import Cliente, Producto, Pedido
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'productos', 'notas']
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
class BuscadorForm(forms.Form):
    q = forms.CharField(label='Buscar cliente por nombre', required=False)
