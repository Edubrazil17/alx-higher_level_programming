#!/usr/bin/python3

import sys

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

def is_safe(board, row, col):
    n = len(board)
    # Check the row
    for j in range(col):
        if board[row][j] == 1:
            return False
    # Check the diagonal from top left to bottom right
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check the diagonal from bottom left to top right
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    def backtrack(col):
        nonlocal solutions
        if col == n:
            solutions.append([row[:] for row in board])
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(col + 1)
                board[row][col] = 0
    backtrack(0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solve_n_queens(n)
    for sol in solutions:
        print_board(sol)
        print()

