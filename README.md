

# TIENDA DE SOUVENIRS

### Eres el desarrollador de un sistema para administrar una tienda de souvenirs turísticos. El sistema debe almacenar y procesar la información de los productos y permitir consultas y cálculos usando únicamente recursividad.

## Atributos del producto
Cada producto tendrá
Código: Identificador único (texto).
Nombre: Nombre del producto.
Categoría: Ej. artesanías, ropa, accesorios, imanes.
Precio: Precio en moneda local.

* Los productos deberán estar precargados y organizados alfabéticamente por nombre para facilitar la búsqueda recursiva.
Operaciones a implementar. Todas las operaciones deben implementarse únicamente con recursión:

1. Búsqueda de un producto por nombre
   * a. Usar búsqueda binaria recursiva (aprovechando el orden alfabético).
   * b. Retornar todos los datos del producto si existe.

2. Cálculo del precio total de todos los productos
   * a. Recorrer recursivamente y acumular el precio total.

3. Cálculo del precio promedio por categoría
   * a. Recorrer recursivamente, contar productos por categoría y sumar precios para luego calcular el promedio.

4. Ordenamiento recursivo por precio
   * a. Implementar QuickSort o MergeSort recursivo.
   * b. Poder ordenar de menor a mayor o viceversa.

5. Búsqueda de productos dentro de un rango de precios
   * a. Retornar una nueva lista recursiva con los productos que cumplen el rango.

6. Generar recomendaciones de compra
   * a. A partir de un producto, recomendar otros de la misma categoría (recorriendo la lista recursivamente).

## Restricciones tecnicas
* No se puede utilizar iteracciones for/while.
* Debe dar solución al menos 2 puntos utilizando tail recursión ó recursión de cola
* Todos los puntos se deben solucionar utilizando recursividad, sin funciones existentes que
realicen toda la operación.

