"""
================================================
MENÚ DE BEBIDAS
================================================
Este archivo contiene la función para gestionar
el menú de bebidas de la pizzería.
"""

from funciones_auxiliares import limpiar_pantalla
from manejo_precios import obtener_precio
import time


def agregar_bebidas(total_bebidas_actual, precios):
    """
    Muestra el menú de bebidas y permite al cliente agregar bebidas.    
    Parámetros:
        total_bebidas_actual (float): Total de bebidas acumulado
        precios (dict): Diccionario con todos los precios    
    Retorna:
        float: El nuevo total de bebidas
    """

    # Obtenemos los precios de las bebidas.
    precio_gaseosa_pers = obtener_precio(precios, "bebidas", "gaseosa_personal")
    precio_gaseosa_fam = obtener_precio(precios, "bebidas", "gaseosa_familiar")
    precio_agua = obtener_precio(precios, "bebidas", "agua")
    
    # Este bucle se repite hasta que el cliente regrese al menú principal.
    while True:
        limpiar_pantalla()
        
        print("=" * 50)
        print("           AGREGAR BEBIDA")
        print("=" * 50)
        print("Seleccione una bebida:")
        print(f"1. Gaseosa Personal (${precio_gaseosa_pers:})")
        print(f"2. Gaseosa Familiar (${precio_gaseosa_fam:})")
        print(f"3. Agua             (${precio_agua:})")
        print("4. Regresar al menú principal")
        print("-" * 50)
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion < 1 or opcion > 4:
                print("¡Opción inválida!... Intente de nuevo.")
                time.sleep(1)
                continue
            
        except ValueError:
            print("ERROR: Debes ingresar un número")
            time.sleep(1)
            continue
        
        # Si eligió regresar.
        if opcion == 4:
            break
        
        # Agregamos el precio de la bebida seleccionada.
        if opcion == 1:
            total_bebidas_actual += precio_gaseosa_pers
        elif opcion == 2:
            total_bebidas_actual += precio_gaseosa_fam
        elif opcion == 3:
            total_bebidas_actual += precio_agua
        
        print(f"¡Bebida agregada! Total bebidas: ${total_bebidas_actual:}")
        time.sleep(1)
    
    return total_bebidas_actual