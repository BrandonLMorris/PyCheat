#!/usr/bin/env python3

DEBUG = True

test_board_solved = [
        [2, 9, 5, 7, 4, 3, 8, 6, 1],
        [4, 3, 1, 8, 6, 5, 9, 2, 7],
        [8, 7, 6, 1, 9, 2, 5, 4, 3],
        [3, 8, 7, 4, 5, 9, 2, 1, 6],
        [6, 1, 2, 3, 8, 7, 4, 9, 5],
        [5, 4, 9, 2, 1, 6, 7, 3, 8],
        [7, 6, 3, 5, 2, 4, 1, 8, 9],
        [9, 2, 8, 6, 7, 1, 3, 5, 4],
        [1, 5, 4, 9, 3, 8, 6, 7, 2]
    ]

test_board_incomplete = [
        [0, 9, 5, 7, 0, 3, 8, 6, 0],
        [4, 3, 1, 8, 6, 5, 9, 2, 7],
        [8, 7, 6, 1, 9, 2, 5, 4, 3],
        [3, 8, 7, 4, 5, 9, 2, 1, 0],
        [6, 1, 0, 3, 8, 7, 4, 9, 5],
        [5, 4, 9, 2, 1, 6, 7, 3, 8],
        [7, 6, 3, 5, 2, 4, 0, 8, 9],
        [9, 2, 8, 6, 7, 1, 3, 5, 4],
        [1, 0, 4, 9, 3, 8, 6, 0, 2]
    ]


def _get_squares(board):
    """Returns the squares of a given board. A square is a 3x3 subsquare
    of the playing board. They are divided into the nine sections seen
    below:

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8
    """
    squares = list()
    for i in range(9):
        start_col = (i % 3) * 3
        start_row = i // 3 * 3
        current = list()
        for j in range(start_row, start_row + 3):
            for k in range(start_col, start_col + 3):
                current.append(board[j][k])
        squares.append(current)

    return squares


def _get_columns(board):
    """Returns a list of the columns of a given board"""
    cols = list()
    for i in range(9):
        col = list()
        for row in board:
            col.append(row[i])
        cols.append(col)
    return cols


def is_valid(board):
    """Returns whether a given sudoku board is valid based on the rules
    of sudoku. Specifically, no row, column, or square can contain
    duplicates of the values 1-9. Blank spots are marked with a 0
    """

    # Every row
    for row in board:
        current = set()
        for i in row:
            assert i >= 0 and i <= 9
            if i in current and i != 0:
                return False
            else:
                current.add(i)

    # Every column
    for col in _get_columns(board):
        current = set()
        for i in col:
            if i in current and i != 0:
                return False
            else:
                current.add(i)

    # Every square
    for square in _get_squares(board):
        current = set()
        for i in square:
            if i in current and i != 0:
                return False
            else:
                current.add(i)

    return True


def verify_solution(board):
    """Verify that a given board is completely solved
    To be a complete solution, every row, column, and square must contain
    the numbers 1-9
    """
    assert len(board) == 9
    complete = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # Every row
    for row in board:
        if not set(row) == complete:
            if DEBUG: print('This one aint right:', 'ROW',  row)
            return False

    # Every column
    for col in _get_columns(board):
        if not set(col) == complete:
            if DEBUG: print('This one aint right', 'COL', col)
            return False

    # Every square
    for square in _get_squares(board):
        if not set(square) == complete:
            if DEBUG: print('This one aint right', 'SQUARE',  square)
            return False

    return True


if __name__ == '__main__':
    print(is_valid(test_board_solved))
    # print(verify_solution(test_board_solved))
    # test_board_solved[0][0] = 7
    # print(verify_solution(test_board_solved))
    # for square in get_squares(test_board_solved):
    #     print(square)
    print(is_valid(test_board_incomplete))
