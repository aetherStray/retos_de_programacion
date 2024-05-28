"""/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""
 
def fibonnaci (objetivo):
    
    penultimo_num = 0
    ultimo_num = 1 
    conmutador = 0

    
    for c in range(objetivo):
        
        if(c == 0 or c == 1):
            print(c)
        else:
            
            print(penultimo_num + ultimo_num)
            
            conmutador = penultimo_num + ultimo_num
            penultimo_num = ultimo_num 
            ultimo_num = conmutador
        
        pass
 
fibonnaci(50)