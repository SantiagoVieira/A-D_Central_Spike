class PermutacionesSinAB:
    def __init__(self):
        pass

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * PermutacionesSinAB.factorial(n - 1)

    @staticmethod
    def permutaciones(n, r):
        return PermutacionesSinAB.factorial(n) // PermutacionesSinAB.factorial(n - r)

    def calcular_permutaciones_sin_ab(self, n):
        total_permutaciones = self.permutaciones(n, n)
        permutaciones_con_AB = 2 * self.permutaciones(n - 1, n - 1)
        permutaciones_sin_AB = total_permutaciones - permutaciones_con_AB
        return permutaciones_sin_AB


def main():
    permutaciones_obj = PermutacionesSinAB()
    n = int(input("Ingrese la cantidad de letras: "))
    resultado = permutaciones_obj.calcular_permutaciones_sin_ab(n)
    print("El número de permutaciones donde A y B no están juntos es:", resultado)

if __name__ == "__main__":
    main()

