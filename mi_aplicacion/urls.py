from django.urls import path
from mi_aplicacion.views import *
from mi_aplicacion import views

urlpatterns = [
    # Actualice los paths en mi aplicacion
    path('', home, name='home'),
    path('nueva_persona/', views.nueva_persona, name='nueva_persona'),
    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('nuevo_pedido/', views.nuevo_pedido, name='nuevo_pedido'),
    path('personas/', views.personas, name='personas'),
    path('productos/', views.productos, name='productos'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('buscar_persona', views.buscar_persona, name='buscar_persona'),
    path('search_persona/', views.search_persona, name='search_persona'),
    path('buscar_pedido', views.buscar_pedido, name='buscar_pedido'),
    path('search_pedido/', views.search_pedido, name='search_pedido'),
    path('buscar_producto', views.buscar_producto, name='buscar_producto'),
    path('search_producto/', views.search_producto, name='search_producto'),
]
