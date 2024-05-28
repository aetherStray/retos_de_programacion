



"""/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */"""



def is_primo(number):
    
    contador = 0
    
    for c in range (1,(number+2)//2):
        
        if(number % c == 0):
            contador += 1
            
    if (contador <= 1):
        print(f"{number} es primo")
    else:
        print(f"{number} no es primo")
        
    pass


for c in range (1,101):
    is_primo(c)
    

