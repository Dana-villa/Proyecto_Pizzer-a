"""
================================================
MANEJO DE PRECIOS - Archivo JSON
================================================
Este archivo maneja la carga y guardado de precios
desde y hacia un archivo JSON.
Es como el sistema de inventario y precios de la pizzería.
"""

import json
import os


# Nombre del archivo donde guardamos los precios
ARCHIVO_PRECIOS = "precios.json"


def crear_precios_iniciales():
    """
    Crea un diccionario con todos los precios iniciales de la pizzería.    
    Retorna:
        dict: Diccionario con todos los precios organizados por categoría
    """
    precios = {
        # Precios de pizzas predeterminadas
        "pizzas_predeterminadas": {
            "margarita": 38000,
            "pepperoni": 20000,
            "hawaiana": 19000,
            "vegetariana": 21000
        },
        
        # Precios según el tamaño de la pizza
        "tamaños": {
            "pequeña": 10000,
            "mediana": 15000,
            "grande": 25000
        },
        
        # Precios de los tipos de masa
        "masas": {
            "delgada": 1000,
            "gruesa": 2000,
            "borde_queso": 5000
        },
        
        # Precios de ingredientes adicionales
        "adicionales": {
            "queso_extra": 3000,
            "champiñones": 3500,
            "jamon": 3000,
            "aceitunas": 4000
        },
        
        # Precios de bebidas
        "bebidas": {
            "gaseosa_personal": 3500,
            "gaseosa_familiar": 5500,
            "agua": 3000
        }
    }
    
    return precios


def cargar_precios():
    """
    Carga los precios desde el archivo JSON.
    Si el archivo no existe, crea uno nuevo con precios iniciales.
    Retorna:
        dict: Diccionario con todos los precios
    """
    try:
        # Intentamos abrir y leer el archivo
        if os.path.exists(ARCHIVO_PRECIOS):
            with open(ARCHIVO_PRECIOS, 'r', encoding='utf-8') as archivo:
                precios = json.load(archivo)
                return precios
        else:
            # Si no existe, creamos uno nuevo
            print("✓ Creando archivo de precios inicial...")
            precios = crear_precios_iniciales()
            guardar_precios(precios)
            return precios
    
    except Exception as e:
        print(f"ERROR al cargar precios: {e}")
        print("Usando precios por defecto...")
        return crear_precios_iniciales()


def guardar_precios(precios):
    """
    Guarda los precios en el archivo JSON.    
    Es como actualizar el libro de precios de la pizzería.    
    Parámetros:
        precios (dict): Diccionario con todos los precios    
    Retorna:
        bool: True si se guardó correctamente
    """
    try:
        with open(ARCHIVO_PRECIOS, 'w', encoding='utf-8') as archivo:
            json.dump(precios, archivo, indent=4, ensure_ascii=False)
        return True
    
    except Exception as e:
        print(f"ERROR al guardar precios: {e}")
        return False


def obtener_precio(precios, categoria, item):
    """
    Obtiene el precio de un item específico. 
    Parámetros:
        precios (dict): Diccionario con todos los precios
        categoria (str): Categoría del producto (pizzas_predeterminadas, tamaños, etc.)
        item (str): Nombre del producto específico.    
    Retorna:
        float: El precio del producto
    """
    try:
        return precios[categoria][item]
    except KeyError:
        print(f"ADVERTENCIA: No se encontró precio para {categoria} - {item}")
        return 0