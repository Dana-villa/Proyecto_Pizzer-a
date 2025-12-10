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
    NOTA: Limpia la pantalla después de que el usuario presiona Enter.
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


def obtener_opcion_valida(min_opcion, max_opcion, mensaje):
    """
    Centraliza la lógica para obtener una opción numérica válida del usuario, 
    eliminando la duplicidad de código en los menús.    
    Parámetros:
        min_opcion (int): El número de opción más bajo permitido.
        max_opcion (int): El número de opción más alto permitido.
        mensaje (str): El mensaje a mostrar al usuario (el prompt).        
    Retorna:
        int: La opción válida seleccionada por el usuario.
    """
    while True:
        try:
            opcion = int(input(mensaje))
            
            if min_opcion <= opcion <= max_opcion:
                return opcion
            else:
                print(f"¡Opción inválida!... Debe estar entre {min_opcion} y {max_opcion}.")
                time.sleep(1)
                
        except ValueError:
            print("ERROR: Debes ingresar un número válido.")
            time.sleep(1)