def min_operaciones(N, cont = 0):
    
    if N == 0:
        return 0
   
    elif N == 1:
        return 1
    
    else:
        
        if N % 2 == 0:
            return 1 + min_operaciones(N // 2 , cont + 1)
        else:
            return 1 + min(min_operaciones(N - 1, cont + 1), min_operaciones(N + 1 , cont + 1))

while True:
  try:
    N = int(input("Ingrese un número: "))
    print(f"Minimo de operaciones: {min_operaciones(N)}")
  except ValueError:
    print("Entrada inválida, por favor ingresa un número válido")
