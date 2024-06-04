



"""/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */"""



def is_primo(number):
    
    if(number == 1):
        print(f"{number} es primo")
        return 0 
    
    for c in range (2,(number+2)//2):
            
        if (number % c == 0):
            print(f"{number} no es primo")
            return 0 
    
    print(f"{number} es primo")
    pass


for c in range (689538005,689538006):
    is_primo(c)
    

