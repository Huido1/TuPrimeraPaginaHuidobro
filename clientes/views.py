from django.shortcuts import render, redirect
from .models import Cliente, Producto, Pedido
from .forms import ClienteForm, ProductoForm, PedidoForm, BuscadorForm
from django.db.models import Q
def home(request):
    return render(request, 'home.html')
def cliente_list(request):
    clientes = Cliente.objects.all().order_by('-created_at')
    return render(request, 'cliente_list.html', {'clientes': clientes})
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})
def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.total = sum([p.precio for p in form.cleaned_data['productos']])
            pedido.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = PedidoForm()
    return render(request, 'pedido_form.html', {'form': form})
def buscar_cliente(request):
    form = BuscadorForm(request.GET or None)
    resultados = []
    q = ''
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            resultados = Cliente.objects.filter(Q(nombre__icontains=q))
    return render(request, 'buscar.html', {'form': form, 'resultados': resultados, 'q': q})
