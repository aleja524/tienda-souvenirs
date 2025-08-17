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