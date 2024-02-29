"""
Find all the ways that one can put n queens on an n by n chessboard
"""

def find_queen_solutions(n):
    solutions = []
    for row in range(n):
        board = [ None ] * n
        board[0] = row
        used_rows = [ False ] * n
        used_rows[row] = True
        for column in range(1, n):
            set_row_index(board, used_rows, column, n)
        solutions.append(board)
    return solutions

def set_row_index(board, used_rows, column, n):
    for row in range(n):
        if used_rows[row]:
            continue
        blocked = False
        for c in range(1, column + 1):
            r_u = row - c
            r_d = row + c
            if board[column - c] == r_u or board[column - c] == r_d:
                blocked = True
                break
        if not blocked:
            board[column] = row
            used_rows[row] = True
            break
    return

def __main__ == '__name__':