"""
==============================================
SISTEMA DE GESTIÓN DE PIZZERÍA
==============================================
Este progrma gestiona los pedidos de una pizzería, permitiendo atender múltiples mesas, personalizar pizzas, agregar bebidas y generar un reporte de cierre de caja.
"""

# Importamos todas las funciones que necesitamos de otros archivos.
from funciones_auxiliares import limpiar_pantalla, pausar, mostrar_total_mesa
from menu_principal import mostrar_menu_principal
from manejo_precios import cargar_precios, guardar_precios



def main():
    """
    Esta es la función principal del programa.
    """

    # Mostramos el titulo del sistema.
    print("=" * 50)
    print("   SISTEMA DE GESTIÓN DE PIZZERÍA")
    print("=" * 50)
    print()
    print("Bienvenido al sistema de pedidos")
    print()

    # Cargamos los precios desde el archivo.
    print("Cargando precios de productos...")
    precios = cargar_precios()
    print("Precios cargados correctamente.")
    print()

    # Esta variable guardará todo el dinero recaudado en el día.
    total_general = 0

    # Limpiamo la pantalla y comenzamos.
    limpiar_pantalla()

    print("=" * 50)
    print("    GESTIÓN DE PEDIDOS")
    print("=" * 50)
    print("Infrese cuántas mesas se atendeán (1 o más): ")

    # Pedimos el número de mesas a atender.
    while True:
        try:
            numero_mesas = int(input("Número de mesas: "))

            # Validamos que sea al menos 1 mesa.
            if numero_mesas < 1:
                print("Por favor, ingrese un número válido (1 o más).")
            else:
                break  # Si es válido, salimos del bucle.
        except ValueError:
            print("ERROR: Debes ingresar un número válido")

    print()

    # Ahora atendermos cada mesa a una.
    # Es como si fuéra de mesa en mesa tomando pedidos.
    for numero_mesa in range(1, numero_mesas + 1):
        # Para cada mesa, iniciamos los totales en cero.
        total_pizzas = 0  # Total de pizzas de esta mesa.
        total_bebidas = 0  # Total de bebidas de esta mesa.
        
        print(f">>> INICIANDO PEDIDO PARA LA MESA N° {numero_mesa} DE {numero_mesas} <<<")
        pausar()

        # Mostramos el menú principal y procesamos el pedido de la mesa.
        # La función retorna los totales de pizzas y bebidas.
        total_pizzas, total_bebidas = mostrar_menu_principal(
            numero_mesa, 
            precios
            )

        # Mostramos el resumen de esta mesa.
        mostrar_total_mesa(total_pizzas, total_bebidas, numero_mesa)

        # Sumamos al total general del día.
        total_general += (total_pizzas + total_bebidas)

        

        # Ya atendimos todas las mesas, ahora mostramos el cierrede caja.
        limpiar_pantalla()
    print("=" * 50)
    print("     CIERRE DE CAJA DEL DÍA")
    print(f"Total de mesas atendidas: {numero_mesas}")
    print("=" * 50)
    print()
    print("Fin del programa... Presione Enter para salir.")
    input()


# Este es el punto de entrada del programa
# Cuando ejecutas este archivo, empieza aquí
if __name__ == "__main__":
    main()