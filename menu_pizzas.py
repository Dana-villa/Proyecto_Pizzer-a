"""
================================================
MENÚ DE PIZZAS PREDETERMINADAS
================================================
Este archivo contiene la función para mostrar y gestionar el menú de pizzas ya preparadas (Margarita, Pepperoni, etc.).
Es como la sección de "Pizzas Especiales" del menú.
"""

from funciones_auxiliares import limpiar_pantalla
from manejo_precios import obtener_precio
import time


def mostrar_menu_pizzas(total_actual, precios):
    """
    Muestra el menú de pizzas predeterminadas y permite al cliente
    agregar pizzas a su pedido.
    Parámetros:
        total_actual (float): El total acumulado hasta ahora
        precios (dict): Diccionario con todos los precios    
    Retorna:
        float: El nuevo total después de agregar pizzas
    """
    # Obtenemos los precios de las pizzas.
    precio_margarita = obtener_precio(precios, "pizzas_predeterminadas", "margarita")
    precio_pepperoni = obtener_precio(precios, "pizzas_predeterminadas", "pepperoni")
    precio_hawaiana = obtener_precio(precios, "pizzas_predeterminadas", "hawaiana")
    precio_vegetariana = obtener_precio(precios, "pizzas_predeterminadas", "vegetariana")

    pizzas = []
    
    # Este bucle se repite hasta que el cliente decida regresar.
    while True:
        limpiar_pantalla()
        
        print("=" * 50)
        print("======  MENÚ DE PIZZAS =======")
        print("=" * 50)
        print(f"1. Pizza Margarita   ${precio_margarita:}")
        print(f"2. Pizza Pepperoni   ${precio_pepperoni:}")
        print(f"3. Pizza Hawaiana    ${precio_hawaiana:}")
        print(f"4. Pizza Vegetariana ${precio_vegetariana:}")
        print("5. Regresar al menú principal")
        print("-" * 50)
        
        # Pedimos que elija una opción.
        try:
            opcion = int(input("Seleccione una opción: "))
            
            # Validamos que la opción sea válida.
            if opcion < 1 or opcion > 5:
                print("¡Opción inválida!... Intente de nuevo.")
                time.sleep(1)
                continue
            
        except ValueError:
            print("ERROR: Debes ingresar un número")
            time.sleep(1)
            continue
        
        # Si eligió regresar, salimos del bucle
        if opcion == 5:
            break
        
        # Agregamos el precio de la pizza seleccionada
        if opcion == 1:
            margarita = {"Pizza_Margarita": precio_margarita}
            total_actual += precio_margarita
            pizzas.append(margarita)
        elif opcion == 2:
            peperoni = {"Pizza_Peperoni": precio_pepperoni}
            total_actual += precio_pepperoni
            pizzas.append(peperoni)
        elif opcion == 3:
            hawaiana = {"Pizza_hawaiana": precio_hawaiana}
            total_actual += precio_hawaiana
            pizzas.append(hawaiana)
        elif opcion == 4:
            vegetariana = {"Pizza_vegetariana": precio_vegetariana}
            total_actual += precio_vegetariana
            pizzas.append(vegetariana)
        print(pizzas)
        
        print(f"¡Pizza agregada!. Total actual: ${total_actual:}")
        time.sleep(1)
    
    return total_actual