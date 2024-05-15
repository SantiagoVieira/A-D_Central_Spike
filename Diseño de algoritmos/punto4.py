def is_valid(board, row, col, num):
    
    for x in range(9):
        if board[row][x] == num:
            return False
    
    for x in range(9):
        if board[x][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def sum_valid(board, target_sum):
    for i in range(9):
        if sum(board[i]) != 0 and sum(board[i]) > target_sum:
            return False
        if sum(row[i] for row in board) != 0 and sum(row[i] for row in board) > target_sum:
            return False
    return True

def solve_sudoku(board, target_sum):
    empty = find_empty_location(board)
    if not empty:
        
        if all(sum(row) == target_sum for row in board) and \
           all(sum(board[i][j] for i in range(9)) == target_sum for j in range(9)):
            return True
        else:
            return False

    row, col = empty
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if sum_valid(board, target_sum) and solve_sudoku(board, target_sum):
                return True
            board[row][col] = 0
    
    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_sudoku(board):
    for row in board:
        print(" ".join(str(num) for num in row))


board = [
    [5, 0, 4],
    [6, 0, 0],
    [0, 9, 0]
]


target_sum = 45

if solve_sudoku(board, target_sum):
    print_sudoku(board)
else:
    print("No existe solución que cumpla con las restricciones dadas.")
