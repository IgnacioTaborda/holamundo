import json

def leer_csv(archivo : str) -> list[list]:
    """Recibe la ruta de un archivo CSV por parametro y retonar una matriz
    con la informacion

    Args:
        archivo (str): Ruta de un archivo CSV

    Returns:
        list[list]: Retorno el archivo en una matriz, donde cada lista 
        representa un renglon.
    """
    ranking = []
    with open(file=archivo, mode="r", encoding="utf-8") as archivo:
        for renglon in archivo.readlines():
            lista = renglon.replace("\n","").split(",")
            lista[1] = int(lista[1]) 
            ranking.append(lista)  
    return ranking   

def escribir_linea(fila : int, matriz : list[list]) -> str:
    """Se encarga de pasar los datos de una fila de una matriz
    a un sting, donde el primer elemento y el segundo estan separados 
    por una coma

    Args:
        fila (int): Número de la fila a convertir
        matriz (list[list]): Matriz que contiene la fila

    Returns:
        str: Retorna los datos de la fila ingresada en un string,
        donde el primer elemento y el segundo estan separados por 
        una coma
    """
    linea = ""
    largo_columnas = len(matriz[0])
    for j in range(largo_columnas):     
        linea += str(matriz[fila][j])
        if j == 0:
            linea += ","
    return linea

def escribir_csv(csv: str, datos: list[list]):
    """Recibe una matriz y la escribe en un archivo CSV

    Args:
        csv (str): Ruta del archivo CSV donde se escribiran los datos
        datos (list[list]): Matriz con los datos a escribir
    """
    with open(file=csv, mode="w", encoding="utf-8") as archivo:
        for i in range(len(datos)):
            linea = escribir_linea(i,datos)
            archivo.write(linea + "\n")

def leer_json(archivo : str) -> dict[dict]:
    """Recibe la ruta de un archivo JSON por parametro y retonar un diccionario
    con el contenido del archivo.

    Args:
        archivo (str): Ruta de un archivo JSON

    Returns:
        dict[dict]: Retorna un diccionario con todo el contenido del arhivo
    """
    with open(file=archivo, mode="r", encoding="utf-8") as archivo:
        jsoncito = json.load(archivo) 
    return jsoncito    

def obtener_elemento_mayor(columna : int, inicio, indice_mayor : int, matriz : list[list], largo_matriz : int):
    """Obtiene el indice de la fila en el que se encuentra el valor más alto de la 
    columna ingresada por parametro

    Args:
        columna (int): Columna en la que se encuentran los valores
        inicio (int): Fila en la que se comienza a evaluar
        indice_mayor (int): Fila en la que esta el mayor elemento y que se usa
        para comparar con el resto de elementos durante la ejecuccion
        matriz (list[list]): Matriz en donde esta la información
        largo_matriz (int): Cantidad de filas de la matriz

    Returns:
        int: Retorna el indice de la fila del número más alto
    """
    for k in range(inicio,largo_matriz):
        if matriz[indice_mayor][columna] < matriz[k][columna]:
            indice_mayor = k
    return indice_mayor

def ordenar_matriz_descendente(matriz : list[list], columna : int) -> list[list]:
    """Recibe una matriz desordenada y la ordena de forma descendente. Solo se evaluan
    los numeros que esten en la columna ingresada por parametro.

    Args:
        matriz (list[list]): Matriz a ordenar
        columna (int): Columna en la que se encuentran los valores

    Returns:
        list[list]: Retorna la matriz ordenada
    """
    largo_matriz = len(matriz)

    for fila in range(largo_matriz - 1):
        indice_elemento_mayor = obtener_elemento_mayor(columna,fila+1,fila,matriz) 
               
        if indice_elemento_mayor != fila:
            aux = matriz[fila]
            matriz[fila] = matriz[indice_elemento_mayor]
            matriz[indice_elemento_mayor] = aux
    return matriz
