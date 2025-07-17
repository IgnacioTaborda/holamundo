import funciones_archivos

def imprimir_ranking(csv_matriz):
    ranking = funciones_archivos.ordenar_matriz_descendente(csv_matriz,1)
    mensaje = f'''
    =================================================
                                                  
        1   -   {ranking[0][0]}   -   {ranking[0][1]}                 
        2   -   {ranking[1][0]}   -   {ranking[1][1]}                                            
        3   -   {ranking[2][0]}   -   {ranking[2][1]}                  
        4   -   {ranking[3][0]}   -   {ranking[3][1]}                    
        5   -   {ranking[4][0]}   -   {ranking[4][1]}                                 
        6   -   {ranking[5][0]}   -   {ranking[5][1]} 
        7   -   {ranking[6][0]}   -   {ranking[6][1]}  
        8   -   {ranking[7][0]}   -   {ranking[7][1]}  
        9   -   {ranking[8][0]}   -   {ranking[8][1]}  
        10  -   {ranking[9][0]}   -   {ranking[9][1]}  
                                                  
    =================================================
    
    '''
    print(mensaje)