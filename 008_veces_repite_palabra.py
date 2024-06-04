"""/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */"""
 
def contador_palabras_repetidas(frase, palabra):
    
    lista = frase.split()
    print(lista)
    print(palabra)
    veces_que_se_repite = 0
    
    for i in range(len(lista)):
        palabra_comparada = str(lista[i].strip().lower)  
        print(palabra_comparada == palabra)
        if(palabra_comparada == palabra.strip().lower):       
            veces_que_se_repite += 1
            
    print(veces_que_se_repite)
    if(veces_que_se_repite > 1):    
        print(f"La palabra se repitio: {veces_que_se_repite} veces")
    else:
        print("La palabra no se repite ni una vez")

contador_palabras_repetidas("Hola bby eres mi mundo entero y siempre te querer bby bby","bby")