from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/nuevo/', views.cliente_create, name='cliente_create'),
    path('productos/nuevo/', views.producto_create, name='producto_create'),
    path('pedidos/nuevo/', views.pedido_create, name='pedido_create'),
    path('buscar/', views.buscar_cliente, name='buscar_cliente'),
]
