  
"""/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */"""
 
def invertir_cadena(cadena):
    
    cadena_invertida = ""
     
    for c in range (len(cadena),0,-1):
        
        print(cadena[c-1], end="")
        
    print("")

invertir_cadena("Hola Mundo")
invertir_cadena("odnuM aloH")