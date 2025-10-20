from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar-compra/', views.agregar_compra, name='agregar_compra'),
    path('buscar-cliente/', views.buscar_cliente, name='buscar_cliente'),
]
