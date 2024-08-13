from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'mi_aplicacion/home.html')

def personas(request):
    return render(request, 'mi_aplicacion/personas.html')

def productos(request):
    return render(request, 'mi_aplicacion/productos.html')

def pedidos(request):
    return render(request, 'mi_aplicacion/pedidos.html')

def nueva_persona(request):
    if request.method == 'POST':
        persona = Persona(nombre=request.POST['nombre'],apellido=request.POST['apellido'],edad=request.POST['edad'],email=request.POST['email']).save()
        return render(request, 'mi_aplicacion/personas.html')
    return render(request, 'mi_aplicacion/nueva_persona.html')

def nuevo_producto(request):
    if request.method == 'POST':
        productos = Producto(nombre=request.POST['nombre'],precio=request.POST['precio'],descripcion=request.POST['descripcion']).save()
        return render(request, 'mi_aplicacion/productos.html')
    return render(request, 'mi_aplicacion/nuevo_producto.html')

def nuevo_pedido(request):
    if request.method == 'POST':
        pedidos = Pedido(persona=request.POST['persona'],producto=request.POST['producto'],fecha_pedido=request.POST['fecha_pedido'],cantidad=request.POST['cantidad']).save()
        return render(request, 'mi_aplicacion/pedidos.html')
    return render(request, 'mi_aplicacion/nuevo_pedido.html')

def buscar_persona(request):
    return render(request, 'mi_aplicacion/buscar_persona.html')

def buscar_pedido(request):
    return render(request, 'mi_aplicacion/buscar_pedido.html')

def buscar_producto(request):
    return render(request, 'mi_aplicacion/buscar_producto.html')

def search_persona(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        apellidos = Persona.objects.filter(nombre__icontains=nombre)
        edades = Persona.objects.filter(nombre__icontains=nombre)
        emails = Persona.objects.filter(nombre__icontains=nombre)
        
        return render(request,"mi_aplicacion/search_persona.html",{"nombre":nombre,"apellidos":apellidos,"edades":edades,"emails":emails})
    else:
        return render(request,"mi_aplicacion/home.html")
     
def search_pedido(request):
    if request.GET["producto"]:
        producto = request.GET["producto"]
        personas = Pedido.objects.filter(producto__icontains=producto)
        fecha_pedidos = Pedido.objects.filter(producto__icontains=producto)
        cantidades = Pedido.objects.filter(producto__icontains=producto)
        
        return render(request,"mi_aplicacion/search_pedido.html",{"producto":producto,"personas":personas,"fecha_pedidos":fecha_pedidos,"cantidades":cantidades})
    else:
        return render(request,"mi_aplicacion/home.html")

def search_producto(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        precios = Producto.objects.filter(nombre__icontains=nombre)
        descripciones = Producto.objects.filter(nombre__icontains=nombre)
        
        return render(request,"mi_aplicacion/search_producto.html",{"nombre":nombre,"precios":precios,"descripciones":descripciones})
    else:
        return render(request,"mi_aplicacion/home.html")
    
    