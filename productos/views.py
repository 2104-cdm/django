from django.shortcuts import render
from productos.models import productos



def entrada(request):
    productos_lista = productos.objects.all()
    return render(request, 'base.html', {'productos': productos_lista})

def usando_create(request):
    productos.objects.create(  
        nombre='koka kola',
        descripcion='refrescante',
        precio=9.99,
        stock=100,
        categoria='soda',
        imagen='http://example.com/imagen.jpg'
    )
    productos_lista = productos.objects.all()
    return render(request, 'base.html', {'productos': productos_lista})  



def usando_save(request):
    producto = productos(
        nombre='koka kola',
        descripcion='refrescante',
        precio=9.99,
        stock=100,
        categoria='soda',
        imagen='http://example.com/imagen.jpg'
    )
    producto.save()
