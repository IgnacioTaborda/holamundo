
def input_consola(mensaje : str, opciones : list) -> str:
    """Pide que se ingrese por consola algo indicado en "mensaje"
    y si lo ingresado se encuentra en "opciones" se retorna.

    Args:
        mensaje (str): Dato a pedir
        opciones (list): Opciones correctas

    Returns:
        str: Si el input se encuentra dentro de opciones lo retorna
    """
    opcion = input(mensaje)
    opcion = opcion.upper()
    if opcion in opciones:
        return opcion
    else:
        opcion = input_consola(mensaje,opciones)
        return opcion
    
