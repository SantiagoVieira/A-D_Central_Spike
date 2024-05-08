import random

def minima_diferencia(A, B):
    A.sort()
    B.sort()

    suma_diferencias = 0

    for i in range(len(A)):
        suma_diferencias += abs(A[i] - B[i])

    return suma_diferencias

n=3
A=[random.randint(1,100) for _ in range(n)]
B=[random.randint(1,100) for _ in range(n)]
print(A)
print(B)
print(minima_diferencia([4,1,8,7],[2,3,6,5]))
