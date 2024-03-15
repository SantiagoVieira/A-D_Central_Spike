`def factorial(n):  # O(n)
    if n == 0 or n == 1:  # O(n)
        return 1  # O(n)
    else:
        return n * factorial(n-1)  # O(n)

def permutaciones(n, r):  # O(n)
    return factorial(n) / factorial(n-r)  # O(n)

def combinaciones(n, r):  # O(n)
    return factorial(n) / (factorial(r) * factorial(n-r))  # O(n)

def main():  # O(n)
    print("1. Permutaciones")  # O(n)
    print("2. Combinaciones")  # O(n)
    opcion = int(input("Elige una opción: "))  # O(1)
    
    if opcion == 1 or opcion == 2:  # O(n)
        n = int(input("Ingresa el valor de n: "))  # O(1)
        r = int(input("Ingresa el valor de r: "))  # O(1)
    
    if opcion == 1:  # O(n)
        print("Permutaciones: ", permutaciones(n, r))  # O(n)
    elif opcion == 2:  # O(n)
        print("Combinaciones: ", combinaciones(n, r))  # O(n)
    else:
        print("Opción no válida")  # O(n)

if __name__ == "__main__":
    main()  # O(n)

`