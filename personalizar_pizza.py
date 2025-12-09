"""
================================================
PERSONALIZACIÓN DE PIZZAS
================================================
Este archivo contiene todas las funciones para que el cliente
pueda crear su pizza personalizada: eligiendo tamaño, masa
y agregando ingredientes adicionales.
"""

from funciones_auxiliares import limpiar_pantalla
from manejo_precios import obtener_precio
import time


def seleccionar_tamaño(precios):
    """
    Permite al cliente elegir el tamaño de su pizza.    
    Parámetros:
        precios (dict): Diccionario con todos los precios    
    Retorna:
        tuple: (precio_seleccionado, continuar)
            - precio_seleccionado: El precio del tamaño elegido
            - continuar: False si el cliente quiere cancelar.
    """

    # Obtenemos los precios de los tamaños.
    precio_peq = obtener_precio(precios, "tamaños", "pequeña")
    precio_med = obtener_precio(precios, "tamaños", "mediana")
    precio_gran = obtener_precio(precios, "tamaños", "grande")
    
    limpiar_pantalla()
    
    print("=" * 50)
    print("        Personaliza tu pizza")
    print("=" * 50)
    print("==========  TAMAÑO PIZZA ===========")
    print(f"1. Pizza Pequeña    ${precio_peq:}")
    print(f"2. Pizza Mediana    ${precio_med:}")
    print(f"3. Pizza Grande     ${precio_gran:}")
    print("4. Cancelar (Regresar al menú principal)")
    print("-" * 50)
    
    while True:
        try:
            opcion = int(input("Seleccione un tamaño: "))
            
            if opcion < 1 or opcion > 4:
                print("¡Opción inválida!... Intente de nuevo.")
                continue
            
            break
        except ValueError:
            print("ERROR: Debes ingresar un número")
    
    # Si eligió cancelar.
    if opcion == 4:
        return 0, False
    
    # Retornamos el precio según la opción elegida.
    if opcion == 1:
        return precio_peq, True
    elif opcion == 2:
        return precio_med, True
    else:  # opcion == 3
        return precio_gran, True


def seleccionar_masa(precios):
    """
    Permite al cliente elegir el tipo de masa.    
    Parámetros:
        precios (dict): Diccionario con todos los precios
    Retorna:
        float: El precio de la masa seleccionada
    """

    # Obtenemos los precios de las masas.
    precio_delgada = obtener_precio(precios, "masas", "delgada")
    precio_gruesa = obtener_precio(precios, "masas", "gruesa")
    precio_borde = obtener_precio(precios, "masas", "borde_queso")
    
    limpiar_pantalla()
    
    print("=" * 50)
    print("===========  TIPO MASA PIZZA ==========")
    print("=" * 50)
    print(f"1. Masa Delgada              ${precio_delgada:}")
    print(f"2. Masa Gruesa               ${precio_gruesa:}")
    print(f"3. Masa con Borde de Queso   ${precio_borde:}")
    print("-" * 50)
    
    while True:
        try:
            opcion = int(input("Seleccione un tipo de masa: "))
            
            if opcion < 1 or opcion > 3:
                print("¡Opción inválida!... Intente de nuevo.")
                continue
            
            break
        except ValueError:
            print("ERROR: Debes ingresar un número")
    
    # Retornamos el precio según la opción.
    if opcion == 1:
        return precio_delgada
    elif opcion == 2:
        return precio_gruesa
    else:  # opcion == 3
        return precio_borde


def seleccionar_adicionales(precios):
    """
    Permite al cliente agregar ingredientes adicionales a su pizza.
    Máximo 4 adicionales permitidos.
    Parámetros:
        precios (dict): Diccionario con todos los precios    
    Retorna:
        float: El total de los adicionales seleccionados
    """

    # Obtenemos los precios de los adicionales.
    precio_queso = obtener_precio(precios, "adicionales", "queso_extra")
    precio_champi = obtener_precio(precios, "adicionales", "champiñones")
    precio_jamon = obtener_precio(precios, "adicionales", "jamon")
    precio_aceitunas = obtener_precio(precios, "adicionales", "aceitunas")
    
    total_adicionales = 0
    contador = 0  # Contador de adicionales agregados.
    
    # Máximo 4 adicionales.
    while contador < 4:
        limpiar_pantalla()
        
        print("=" * 50)
        print("      SELECCIÓN DE ADICIONALES")
        print("=" * 50)
        print(f"Adicionales seleccionados: {contador}/4")
        print()
        print(f"1. Queso extra   (${precio_queso:})")
        print(f"2. Champiñones   (${precio_champi:})")
        print(f"3. Jamón         (${precio_jamon:})")
        print(f"4. Aceitunas     (${precio_aceitunas:})")
        print("5. Finalizar adicionales")
        print("-" * 50)
        
        try:
            opcion = int(input("Seleccione un adicional: "))
            
            if opcion < 1 or opcion > 5:
                print("¡Opción inválida!... Intente de nuevo.")
                time.sleep(1)
                continue
            
        except ValueError:
            print("ERROR: Debes ingresar un número")
            time.sleep(1)
            continue
        
        # Si eligió finalizar.
        if opcion == 5:
            break
        
        # Agregamos el precio del adicional seleccionado
        if opcion == 1:
            total_adicionales += precio_queso
        elif opcion == 2:
            total_adicionales += precio_champi
        elif opcion == 3:
            total_adicionales += precio_jamon
        elif opcion == 4:
            total_adicionales += precio_aceitunas
        
        contador += 1
        print(f"¡Adicional agregado!. Total adicionales: ${total_adicionales:}")
        print(f"Adicionales seleccionados: {contador}/4")
        time.sleep(1)
    
    # Si llegó al límite de 4.
    if contador == 4:
        print()
        print("¡Límite de 4 adicionales alcanzado!... Finalizando selección.")
        time.sleep(2)
    
    print()
    print("Disfruta tu Pizza Personalizada.")
    time.sleep(1)
    
    return total_adicionales


def personalizar_pizza(total_actual, precios):
    """
    Función principal que coordina todo el proceso de personalización.    
    Parámetros:
        total_actual (float): El total acumulado hasta ahora
        precios (dict): Diccionario con todos los precios    
    Retorna:
        float: El nuevo total después de personalizar la pizza
    """

    # Este bucle permite crear múltiples pizzas personalizadas.
    while True:
        # Paso 1: Seleccionar tamaño.
        precio_tamaño, continuar = seleccionar_tamaño(precios)
        
        # Si el cliente decidió cancelar.
        if not continuar:
            break
        
        # Agregamos el precio del tamaño al total.
        total_actual += precio_tamaño
        
        # Paso 2: Seleccionar masa.
        precio_masa = seleccionar_masa(precios)
        total_actual += precio_masa
        
        print(f"Masa agregada. Total actual: ${total_actual:}")
        time.sleep(1)
        
        # Paso 3: Seleccionar adicionales.
        precio_adicionales = seleccionar_adicionales(precios)
        total_actual += precio_adicionales
        
        # Preguntamos si quiere personalizar otra pizza.
        limpiar_pantalla()
        print(f"Total actual con pizza personalizada: ${total_actual:}")
        print()
        respuesta = input("¿Desea personalizar otra pizza? (S/N): ").upper()
        
        if respuesta != 'S':
            break
    
    return total_actual
