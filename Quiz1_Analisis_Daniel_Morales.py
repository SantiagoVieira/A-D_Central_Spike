#4x^2 + 12x + 8
#4(x+1)(x+2) 
#x+1 = 0  x+2 = 0
#x=-1  x=-2
#Xn = C1(-1)^n + C2(-2)^n
#X0 = 6  X1 = 7
#6 = C1(-1)^0 + C2(-2)^0
#(1)  6 = -C1 - C2
#7 = C1(-1)^1 + C2(-2)^1
#(2)  7 = -C1 - 2C2

#Sistema de ecuaciones
#6 = -C1 - C2 (-1) 
#7 = -C1 - 2C2

#-6 = C1 + C2
#7 = -C1 - 2C2

#1 = 0 - C2
#C2 = -1

#Remplazamos en (1)

#6 = C1 - 1
#6 + 1  = C1
#C1 = 7

#X1500 = 7(-1)^1500 - 1(-2)^1500 = -7+2^1500

#-------------------------------------------------------------------------------------

def encontrar_mayus(text):
    if text == "":
        return []
    else:
        if text[0].isupper():
            return [(text[0], 0)] + encontrar_mayus(text[1:])
        else:
            return encontrar_mayus(text[1:])
         

print(encontrar_mayus(""))
print(encontrar_mayus("Profe Poneme un 5"))

#----------------------------------------------------------------------------------

def factorial(num):                  
    if num == 0 or num == 1:           
        return 1                       
    else:
        resultado = 1                  
        for i in range(2, num + 1):    
            resultado *= i             
        return resultado 

def combinaciones_no_repetida(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))  

print(combinaciones_no_repetida(9, 4))


