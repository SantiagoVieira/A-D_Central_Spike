def is_valid(matrix, row, col, num):
    
    if num in matrix[row]:
        return False
    
    
    for i in range(len(matrix)):
        if matrix[i][col] == num:
            return False
    
    return True

def fill_matrix(matrix, row, col):
    
    if row == len(matrix):
        return sum(matrix[0]) == sum(matrix[1]) == sum(matrix[2]) == 14
    
    
    next_row = row + (col + 1) // len(matrix)
    next_col = (col + 1) % len(matrix)
    
    
    if matrix[row][col] != 0:
        return fill_matrix(matrix, next_row, next_col)
    
    
    for num in range(1, 10):
        if is_valid(matrix, row, col, num):
            matrix[row][col] = num
            if fill_matrix(matrix, next_row, next_col):
                return True
            matrix[row][col] = 0
    
    return False

def print_matrix(matrix):
    for row in matrix:
        print(row)

def solve(matrix):
    if fill_matrix(matrix, 0, 0):
        print("Solución encontrada:")
        print_matrix(matrix)
    else:
        print("No se encontró solución.")


a = [
    [5, 0, 2],
    [8, 5, 0],
    [0, 2, 0]
]

solve(a)
