"""
================================================
MENÚ PRINCIPAL
================================================
Este archivo contiene la función del menú principal
que coordina todas las opciones disponibles:
- Pizzas predeterminadas
- Personalizar pizza
- Agregar bebidas
- Ver total y salir
"""

from funciones_auxiliares import limpiar_pantalla
from menu_pizzas import mostrar_menu_pizzas
from personalizar_pizza import personalizar_pizza
from menu_bebidas import agregar_bebidas


def mostrar_menu_principal(numero_mesa, precios):
    """
    Muestra el menú principal y gestiona las opciones del cliente.    
    Parámetros:
        numero_mesa (int): Número de la mesa que estamos atendiendo
        precios (dict): Diccionario con todos los precios    
    Retorna:
        tuple: (total_pizzas, total_bebidas)
    """

    # Iniciamos los totales en cero.
    total_pizzas = 0
    total_bebidas = 0
    
    # Este bucle se repite hasta que el cliente pida la cuenta.
    while True:
        limpiar_pantalla()
        
        # Calculamos el total general de la mesa.
        total_mesa = total_pizzas + total_bebidas
        
        print("=" * 50)
        print("    BIENVENIDO A TU PIZZERIA")
        print("=" * 50)
        print(f"MENÚ PRINCIPAL (Mesa {numero_mesa} - Total: ${total_mesa:})")
        print()
        print("1. Ver menú de pizzas")
        print("2. Personaliza tu pizza")
        print("3. Agregar bebida")
        print("4. Ver total y SALIR")
        print("-" * 50)
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion < 1 or opcion > 4:
                print("¡Opción inválida!... Intente de nuevo.")
                input("Presione Enter para continuar...")
                continue
            
        except ValueError:
            print("ERROR: Debes ingresar un número")
            input("Presione Enter para continuar...")
            continue
        
        # Ejecutamos la acción según la opción elegida.
        if opcion == 1:
            # Ver menú de pizzas predeterminadas.
            total_pizzas = mostrar_menu_pizzas(total_pizzas, precios)
        
        elif opcion == 2:
            # Personalizar pizza.
            total_pizzas = personalizar_pizza(total_pizzas, precios)
        
        elif opcion == 3:
            # Agregar bebidas.
            total_bebidas = agregar_bebidas(total_bebidas, precios)
        
        elif opcion == 4:
            # Ver total y salir.