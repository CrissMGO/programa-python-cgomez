# ============================================================
# Universidad Nacional Abierta y a Distancia - UNAD
# Curso: Fundamentos de Programacion (213022)
# Fase 5 - Evaluacion Final POA
# Problema 3: Auditoria de inventario y calculo de pedidos
# Estudiante: Cristian Gomez
# Fecha: Mayo de 2026

# ===========================================================


def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Modulo (funcion) que calcula la cantidad exacta de unidades
    a pedir para reabastecer un articulo.

    Parametros:
        stock_actual (int): unidades disponibles actualmente.
        stock_minimo (int): unidades minimas requeridas en bodega.

    Retorna:
        int: cantidad a pedir. Sera 0 si el stock es suficiente,
             o (stock_minimo - stock_actual) si esta por debajo.
    """
    # Estructura condicional: aplica la logica de negocio.
    if stock_actual < stock_minimo:
        # Caso 1: el stock actual es insuficiente -> calcular faltante.
        cantidad = stock_minimo - stock_actual
    else:
        # Caso 2: el stock actual cubre el minimo -> no se pide nada.
        cantidad = 0

    return cantidad


def generar_reporte_pedidos(inventario):
    """
    Recorre la matriz de inventario y muestra el reporte
    de pedidos de reabastecimiento.

    Parametros:
        inventario (list): matriz con filas
                           [Codigo, Nombre, Stock Actual, Stock Minimo].
    """
    # Encabezado del reporte.
    print("=" * 65)
    print("        REPORTE DE PEDIDOS DE REABASTECIMIENTO")
    print("=" * 65)
    print(f"{'Codigo':<10}{'Articulo':<22}{'Stock':<10}{'Minimo':<10}{'Pedir':<10}")
    print("-" * 65)

    # Acumuladores para mostrar un resumen al final.
    total_unidades = 0
    articulos_a_pedir = 0

    # Estructura repetitiva: recorre cada fila de la matriz.
    for articulo in inventario:
        # Desempaquetado de los datos de cada articulo.
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        # Se invoca el modulo para calcular la cantidad a pedir.
        cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

        # Se imprime la fila correspondiente al articulo.
        print(f"{codigo:<10}{nombre:<22}{stock_actual:<10}{stock_minimo:<10}{cantidad:<10}")

        # Si la cantidad es mayor que cero, se actualizan los acumuladores.
        if cantidad > 0:
            total_unidades = total_unidades + cantidad
            articulos_a_pedir = articulos_a_pedir + 1

    # Cierre y resumen del reporte.
    print("-" * 65)
    print(f"Articulos que requieren reposicion: {articulos_a_pedir}")
    print(f"Total de unidades a pedir:          {total_unidades}")
    print("=" * 65)


# ============================================================
# Programa principal
# ============================================================
def main():
    """
    Punto de entrada del programa. Define la matriz de inventario
    e invoca el modulo que genera el reporte de pedidos.
    """
    # Matriz (arreglo bidimensional) con 6 articulos.
    # Cada fila tiene: [Codigo, Nombre, Stock Actual, Stock Minimo].
    inventario = [
        ["A001", "Tornillos M5",        45, 100],
        ["A002", "Tuercas M5",         120,  80],
        ["A003", "Arandelas planas",    30,  50],
        ["A004", "Pernos hexagonales",  15,  40],
        ["A005", "Brocas 1/4",          60,  60],
        ["A006", "Sierra circular",      2,   5],
    ]

    # Se llama al modulo que recorre la matriz y emite el reporte.
    generar_reporte_pedidos(inventario)


# Punto de inicio de la ejecucion: solo corre si el archivo se
# ejecuta directamente (no si se importa desde otro modulo).
if __name__ == "__main__":
    main()
