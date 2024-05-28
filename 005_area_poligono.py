"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
 """
 
def area_poligono(tipo_poligono, value1, value2 = 0):
    
    if (tipo_poligono == "cuadrado"):
        return value1 * value1
    
    elif(tipo_poligono == "triangulo"):
        return value1 * value2 / 2
    
    elif(tipo_poligono == "rectangulo"):
        return value1 * value2

print(area_poligono("cuadrado", 5)) 
print(area_poligono("triangulo", 5, 10))
print(area_poligono("rectangulo", 5, 10))