import auxiliares as aux
import variables as var

def imprimir_pantalla_menu():
    """Imprime el menu principal del juego
    """
    menu = '''
    ================================================
    ║                                              ║
    ║              DRAGON BALL Z TCG               ║
    ║                                              ║
    ║                   -Juego-                    ║
    ║                  -Ranking-                   ║
    ║                  -Opciones-                  ║  
    ║                   -Cerrar-                   ║
    ║                                              ║ 
    ================================================
    '''
    print(menu)
    


def menu() -> str:
    """Muestra el menu del juego por consola y pide que se ingrese
    una opcion para acceder a diferentes pantallas del juego o para 
    cerrarlo.

    Returns:
        str: Retorna la opción ingresada, siempre y cuando forme parte
        de la lista de opciones.
    """
    imprimir_pantalla_menu()
    opcion = aux.input_consola(var.MENSAJE_MENU, var.OPCIONES_MENU)
    return opcion

