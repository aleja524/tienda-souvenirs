class Producto:
    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    
    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - {self.categoria} - ${self.precio}"
    
def busqueda_binaria(productos, nombre, inicio= 0, fin= None):
    
    if fin is None:
        fin = len(productos) - 1
    
    if inicio > fin:
        return None
    
    mid = (inicio + fin) // 2
    actual = productos[mid]

    if actual.nombre == nombre:
        return actual
    
    if nombre < actual.nombre:
        return busqueda_binaria(productos, nombre, inicio, mid - 1)
    else:
        return busqueda_binaria(productos, nombre, mid + 1, fin)


def precio_total(productos, i=0, acumulado=0):
    if i == len(productos):
        return acumulado
    
    nuevo_acumulado = acumulado + productos[i].precio
    return precio_total(productos, i + 1, nuevo_acumulado)


def promedio_categoria(productos, categoria, i=0, suma=0, cantidad=0):
    if i == len(productos):
        if cantidad == 0:
            return 0
        return suma / cantidad
    
    if productos[i].categoria == categoria:
        nuevo_suma = suma + productos[i].precio 
        nueva_cantidad = cantidad + 1
        return promedio_categoria(productos, categoria, i + 1, nuevo_suma, nueva_cantidad)
    else:
        return promedio_categoria(productos, categoria, i + 1, suma, cantidad)


def ordenamiento_precio(productos, ascendente=True):
    if len(productos) <= 1:
        return productos
    
    pivote = productos[0]
    resto = productos[1:]

    def partir(productos, i = 0, menores = None, mayores = None):
        if menores is None: menores = []
        if mayores is None: mayores = []

        if i == len(productos):
            return menores, mayores
        
        actual = productos[i]
        if actual.precio < pivote.precio:
            return partir(productos, i + 1, menores + [actual], mayores)
        else:
            return partir(productos, i + 1, menores, mayores + [actual])
    
    menores, mayores = partir(resto)

    izquierda = ordenamiento_precio(menores, ascendente)
    derecha = ordenamiento_precio(mayores, ascendente)

    if ascendente:
        return izquierda + [pivote] + derecha
    else:
        return derecha + [pivote] + izquierda


def productos_en_rango(productos, minimo, maximo, i=0):
    if i == len(productos):
        return []
    actual = productos[i]

    if actual.precio >= minimo and actual.precio <= maximo:
        return [actual] + productos_en_rango(productos, minimo, maximo, i + 1)
    else:
        return productos_en_rango(productos, minimo, maximo, i + 1) 


def recomendaciones(productos, producto_base, i=0, resultado=None):
    if i == len(productos):
        return []
    actual = productos[i]

    if actual.categoria == producto_base.categoria and actual != producto_base:
        return [actual] + recomendaciones(productos, producto_base, i + 1)
    else:
        return recomendaciones(productos, producto_base, i + 1)

def imprimir_productos(productos, i=0):
    if i == len(productos):
        return
    print(productos[i])
    imprimir_productos(productos, i+1)



productos = [
    Producto("001", "Artesania maya", "artesanias", 15000),
    Producto("004", "bufanda andina", "ropa", 25000),
    Producto("002", "Camisa bordada", "ropa", 40000),
    Producto("003", "iman medellin", "imanes", 8000),
]


if __name__ == "__main__":
    print("Lista de productos (ordenados):")
    imprimir_productos(productos)

    buscado = "bufanda andina"
    encontrado = busqueda_binaria(productos, buscado)
    if encontrado:
        print(f"Producto encontrado: {encontrado}")
    else:
        print(f"'{buscado}' no está en la lista")

    # Prueba precio total
    total = precio_total(productos)
    print("\nPrecio total de todos los productos:", total)

    # Prueba promedio por categoría
    categoria = "ropa"
    promedio = promedio_categoria(productos, categoria)
    print(f"\nPrecio promedio de la categoría '{categoria}': {promedio}")

    # Prueba búsqueda en rango
    minimo, maximo = 10000, 30000
    print(f"\nProductos con precio entre {minimo} y {maximo}:")
    en_rango = productos_en_rango(productos, minimo, maximo)
    imprimir_productos(en_rango)

    # Prueba recomendaciones
    producto_base = productos[1]  # Camisa bordada
    print(f"\nRecomendaciones para '{producto_base.nombre}':")
    recomendados = recomendaciones(productos, producto_base)
    imprimir_productos(recomendados)

    # Prueba ordenamiento asc
    print("\nProductos ordenados de menor a mayor precio:")
    ordenados_asc = ordenamiento_precio(productos, ascendente=True)
    imprimir_productos(ordenados_asc)

    # Prueba ordenamiento desc
    print("\nProductos ordenados de mayor a menor precio:")
    ordenados_desc = ordenamiento_precio(productos, ascendente=False)
    imprimir_productos(ordenados_desc)