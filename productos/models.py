from django.db import models

# Create your models here.
class productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.URLField(blank=True, null=True)
    
    
class PedidosProductos(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos', on_delete=models.CASCADE)
    cantidad = models.IntegerField()


class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('P', 'Pendiente'),
        ('E', 'Enviado'),
        ('D', 'Entregado'),

    ]

    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=ESTADOS_PEDIDO, default='P')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    productos = models.ManyToManyField(productos, through='PedidosProductos')
    
    
    
    
