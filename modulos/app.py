import os
import pantallas.pantalla_menu as pantalla_menu
   
def dragon_ball_tcg():
    ejecutandose = True
    pantalla_actual = "MENU"
    
    while ejecutandose:
        match pantalla_actual:
            
            case "MENU":
                pantalla_actual = pantalla_menu.menu()
            
            case "JUEGO":
                # archivo_json = archivos_fun.leer_json(var.JSON)
                # hero = card.armar_mazo_aleatorio(archivo_json.get("cantidades"), archivo_json.get("rutas_cartas"))
                # villano = card.armar_mazo_aleatorio(archivo_json.get("cantidades"), archivo_json.get("rutas_cartas"))

                # juego = combatito.combate(hero,villano)
                
                # ranking["puntuacion"] = juego.get("puntuacion_total")
                # pantalla_actual = juego.get("pantalla_actual")
                # ranking["activar"] = True
                pass
            
            case "OPCIONES":
                print("OPCIONANDO")
            
            case "RANKING":
                print("RANKEANDO")
            
            case "CERRAR":
                ejecutandose = False
                print("Hasta la proximaaa!")
                
        os.system('pause')
                
dragon_ball_tcg()