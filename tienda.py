class Producto:
    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    
def __str__(self):
    return f"[{self.codigo}] {self.nombre} - {self.categoria} - {self.precio}"
    
def busqueda_binaria(productos, nombre, inicio= 0, fin= None):
    pass

def precio_total(productos, i=0, acumulado=0):
    pass

def promedio_categoria(productos, categoria, i=0, suma=0, cantidad=0):
    pass

def ordenamiento_precio(productos, ascendente=True):
    pass

def productos_en_rango(productos, minimo, maximo, i=0, resultado=None):
    pass

def recomendaciones(productos, producto_base, i=0, resultado=None):
    pass

def imprimir_productos(productos, i=0):
    if i == len(productos):
        return
    print(productos[i])
    imprimir_productos(productos, i+1)



productos = [
    Producto("001", "Artesania maya", "artesanias", "artesanias", 15000),
    Producto("002", "Camisa bordada", "ropa", 40000),
    Producto("003", "iman medellin", "imanes", 8000),
    Producto("004", "bufanda andina", "ropa", 25000)
]


