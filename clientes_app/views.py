from django.shortcuts import render
from .models import Cliente, Producto, Compra
from .forms import ClienteForm, ProductoForm, CompraForm, BuscarClienteForm

def inicio(request):
    return render(request, 'clientes_app/inicio.html')

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'clientes_app/formulario.html', {'form': form, 'titulo': 'Agregar Cliente'})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()
    return render(request, 'clientes_app/formulario.html', {'form': form, 'titulo': 'Agregar Producto'})

def agregar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CompraForm()
    return render(request, 'clientes_app/formulario.html', {'form': form, 'titulo': 'Registrar Compra'})

def buscar_cliente(request):
    resultados = None
    if request.method == 'POST':
        form = BuscarClienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados = Cliente.objects.filter(nombre__icontains=nombre)
    else:
        form = BuscarClienteForm()
    return render(request, 'clientes_app/buscar.html', {'form': form, 'resultados': resultados})
