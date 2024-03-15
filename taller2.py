class CalculadoraCombinatoria:
    def __init__(self, n, r):
        self.n = n
        self.r = r

    def factorial(self, num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * self.factorial(num-1)

    def permutaciones(self):
        return self.factorial(self.n) / self.factorial(self.n-self.r)

    def combinaciones(self):
        return self.factorial(self.n) / (self.factorial(self.r) * self.factorial(self.n-self.r))

    def variaciones(self):
        return self.factorial(self.n) / self.factorial(self.n-self.r)

class InterfazUsuario:
    def __init__(self):
        self.calculadora = None

    def solicitar_datos(self):
        print("1. Permutaciones")
        print("2. Combinaciones")
        print("3. Variaciones")
        opcion = int(input("Elige una opción: "))
    
        if opcion in [1, 2, 3]:
            n = int(input("Ingresa el valor de n: "))
            r = int(input("Ingresa el valor de r: "))
            self.calculadora = CalculadoraCombinatoria(n, r)
        
        return opcion

    def mostrar_resultado(self, opcion):
        if opcion == 1:
            print("Permutaciones: ", self.calculadora.permutaciones())
        elif opcion == 2:
            print("Combinaciones: ", self.calculadora.combinaciones())
        elif opcion == 3:
            print("Variaciones: ", self.calculadora.variaciones())
        else:
            print("Opción no válida")

def main():
    interfaz = InterfazUsuario()
    opcion = interfaz.solicitar_datos()
    interfaz.mostrar_resultado(opcion)

if __name__ == "__main__":
    main()
