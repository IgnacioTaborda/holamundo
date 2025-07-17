import os
import random

def extraer_datos_carta(archivo : list) -> dict:
    """Crea un diccionario que contiene las stats de la carta

    Args:
        archivo (list): Lista que contiene las stats de la carta

    Returns:
        dict: Retorna un diccionario que tiene las stats
        de la carta
    """
    carta = {
        "ID" : archivo[0],
        "HP" : archivo[2],
        "ATK" : archivo[4],
        "DEF" : archivo[6],
        "Bonus" : int(archivo[7]),
    }
    return carta

def armar_mazo_carpeta(ruta_carpeta : str) -> dict[dict]:
    """Crea un diccionario que contiene sub-diccionarios con cartas y 
    sus stats.

    Args:
        ruta_carpeta (str): Ruta de la carpeta que tiene las cartas

    Returns:
        dict[dict]: Retorna un diccionario que tiene sub-diccionarios
        que contienen cartas con sus valores (ID, HP, ATK, DEF y BONUS)
    """

    mazo_dict = {}
    contador = 1

    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, archivo) #literalmente es la ruta del archivo
        
        if os.path.isfile(ruta_archivo):
            archivo = archivo.replace(".png","")
            archivo = archivo.split("_")
            largo_archivo = len(archivo)
            
            if largo_archivo == 8:
                archivo = extraer_datos_carta(archivo)
                mazo_dict[contador] = archivo
                contador += 1
    return mazo_dict

def armar_mazo_aleatorio(cantidades: dict, cartas_rutas: dict) -> dict:
    """Crea un mazo aleatorio respetando las "cantidades" del diccionario.

    Args:
        cantidades (dict): Diccionario con las cantidades de cartas por expansión.
        cartas_rutas (dict): Diccionario con las rutas de las cartas y sus stats.

    Returns:
        dict: Mazo aleatorio generado con las cartas especificadas por cantidad.
    """
    mazo_aleatorio = {}

    for nombre_mazo, cantidad in cantidades.items():
        if nombre_mazo in cartas_rutas:
            ruta = cartas_rutas[nombre_mazo]
            cartas_mazo = armar_mazo_carpeta(ruta)
            mazo_aleatorio[nombre_mazo] = random.sample(list(cartas_mazo.values()), cantidad)
    
    return mazo_aleatorio

def unificar_cartas(mazo: dict) -> list:
    """_summary_

    Args:
        mazo (dict): _description_

    Returns:
        list: Lista que contiene las cartas con su valores
    """
    cartas_mazo = []
    for cartas in mazo.values():
        cartas_mazo.extend(cartas)
    random.shuffle(cartas_mazo) #REORDENA ALEATORIAMENTE UNA LISTA
    return cartas_mazo

def sumar_stats_totales(cartas: list) -> dict:
    """Suma las stats totales del mazo."""
    total = {"HP": 0, "ATK": 0, "DEF": 0}
    for carta in cartas:
        total["HP"] += int(carta["HP"])
        total["ATK"] += int(carta["ATK"])
        total["DEF"] += int(carta["DEF"])
    return total