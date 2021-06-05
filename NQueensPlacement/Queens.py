
from sys import stdin, stdout
from copy import deepcopy

def was_valid_placement(current_placements):
    if len(current_placements) == 1:
        return True
    latest_column_index = len(current_placements) - 1
    latest_row_index    = current_placements[latest_column_index]
    for x in range(len(current_placements) - 1):
        if current_placements[x] == latest_row_index:
            return False
        if abs(x - latest_column_index) == abs(current_placements[x] - latest_row_index):
            return False
    return True
"""Here n denotes the size of the chessboard.
    i denotes row placement of a queen in the chess board.
    kth index in current_placements denotes the column of the kth queen in the current_placements.
    The kth value in current_placements denotes the row of the kth queen."""

def place_queen(current_placements, n, solutions):
    if (len(current_placements) == n):
        return solutions.append(current_placements)
    for i in range(n):
        current_placements.append(i)
        if (was_valid_placement(current_placements)):
            place_queen(deepcopy(current_placements), n, solutions)
        current_placements.pop()

def main():
    n = [int(x) for x in stdin.readline().split()][0]
    board     = []
    solutions = []
    place_queen(board, n, solutions)
    for i in solutions:
        print(i)
main()
