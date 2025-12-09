"""
Este archivo contiene funciones de utilidad que se usan en diferentes partes del programa, como limpiar pantalla, hacer pausas y mostrar resumenes.
"""

import os  # Para limpiar pantalla.
import time  # Para hacer pausas.


def limpiar_pantalla():
    """
    Limpia la pantalla de la consola para que se vea más ordenado.
    """

    # Si estamos en Windows, usamos 'cls', si no, usamos 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')



def pausar():
    """
    Hace una pausa para que el usuario pueda leer mensajes.
    """

    print()
    input("Presione Enter para continuar...")
    limpiar_pantalla()



def mostrar_total_mesa(total_pizzas, total_bebidas, numero_mesa):
    """
    Muestra el resumen del peido de una mesa específica.
    Parámetros:
        total_pizzas (float): Total gastado en pizzas.
        total_bebidas (float): Total gastado en bebidas.
        numero_mesa (int): Número de la mesa.
    """

    print("=" * 50)
    print(f"   RESUMEN DEL PEDIDO DE LA MESA N° {numero_mesa}")
    print("=" * 50)
    print(f"Total de pizzas: ${total_pizzas:}")
    print(f"Total de bebidas: ${total_bebidas:}")
    print("-" * 50)
    print(f"Total General de la Mesa: ${total_pizzas + total_bebidas:}")
    print("=" * 50)
    print(f"¡Gracias por visitarnos, Mesa {numero_mesa}!")
    print()

    # Esperamos 3 segundos para que puedan leer el resumen.
    time.sleep(3)    