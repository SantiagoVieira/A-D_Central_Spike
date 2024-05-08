def encontrar_minimo(arr):
    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return arr[0]

    medio = len(arr) // 2
    izquierda_medio = arr[:medio]
    derecho_medio = arr[medio:]

    minimo_izquierdo = encontrar_minimo(izquierda_medio)
    minimo_derecho = encontrar_minimo(derecho_medio)

    if minimo_izquierdo is None:
        return minimo_derecho
    elif minimo_derecho is None:
        return minimo_izquierdo
    else:
        return minimo_izquierdo if minimo_izquierdo < minimo_derecho else minimo_derecho


lista = [8, 3, 6, 2, 7, 1, 5, 4]
print("El minimo de la lista entregada es :", encontrar_minimo(lista))
