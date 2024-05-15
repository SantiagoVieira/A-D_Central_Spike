def ruta_maxima(n, matriz):
    bt = [[0] * n for _ in range(n)]

    for j in range(n):
        bt[0][j] = matriz[0][j]

    for i in range(1, n):
        for j in range(n):
            bt[i][j] = matriz[i][j] + max(bt[i - 1][j], bt[i - 1][max(0, j - 1)], bt[i - 1][min(n - 1, j + 1)])

    return max(bt[n - 1])


n = 2
# matriz = [[348, 391],
#         [618, 193]]

matriz_2 = [[2, 2],
            [2, 2]]

print(ruta_maxima(n, matriz_2))
