from decimal import Decimal, getcontext

class TerminoNesimo:
    def __init__(self):
        self.n = 0

    def solicitar_termino_nesimo(self):
        self.n = int(input("Ingrese el término n-ésimo: "))

    def calcular_formula(self):
        getcontext().prec = 15
        term1 = Decimal(12) * Decimal(-0.5) ** self.n
        term2 = Decimal(-4) * Decimal(-3) ** self.n
        formula = term1 + term2
        return formula

    def mostrar_resultado(self, resultado):
        print("El resultado del término n-ésimo es:", resultado)


def main():
    while True:
        termino = TerminoNesimo()
        termino.solicitar_termino_nesimo()
        resultado = termino.calcular_formula()
        termino.mostrar_resultado(resultado)


        continuar = input("¿Desea calcular otro término? (s/n): ")
        if continuar.lower() != 's':
            print("¡la buena juanca!")
            break

if __name__ == "__main__":
    main()
