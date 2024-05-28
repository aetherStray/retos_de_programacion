"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""
 
def es_anagrama(cadena1, cadena2):
    
    
    for c in cadena1.lower():
        
        if (c not in cadena2.lower()):
            return False
    
    if (len(cadena1) == len(cadena2)):
        return True
    else:
        return False        
     
print(es_anagrama("Quieren", "enrique"))