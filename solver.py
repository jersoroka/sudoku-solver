'''Solves the sudoku board if solvable.'''

import copy
from typing import List


# ---FUNCTIONS---

class Board:
    '''
    A class used to represent a sudoku board

    ...

    Attributes
    ----------
    board : list
        a list of all the values filled in on the sudoku board
    path : list
        a list of the previous board in path to current board
    visited : list
        a list of all previous boards that have been checked


    Methods
    -------
    square(row_slice, pos_slice)
        Produces a 3x3 section of the sudoku board
    '''

    def __init__(self, board, path, visited):
        '''
        Parameters
        ----------
        board : list
            a list of all the values in a sudoku board
        path : list
            a list of the previous board in path to current board
        visited : list
            a list of all previous boards that have been checked
        '''

        self.board = board
        self.path = path
        self.visited = visited

    @staticmethod
    def square(bd: List[int],
               row_slice: List[int],
               pos_slice: List[int]) -> List[List[int]]:
        '''Produces a 3x3 section of the sudoku board

        Args:
            bd : a list of all the values in a sudoku board
            row_slice : a range of rows used to form the square, where
                        row_slice[0] is the first row and
                        (row_slice[1] - 1) is the last row
            pos_slice : a range of indexes corresponding to values used to
                        form the square, where pos_slice[0] is the index of
                        the first value and (pos_slice[1] - 1) is the index
                        of the last value
        Returns:
            list containing all the values within row_slice and pos_slice
            of the board (3x3 square)
        '''

        return [row[index] for row in bd[row_slice[0]: row_slice[1]]
                for index in range(pos_slice[0], pos_slice[1])]


def solver(bd: List[int]) -> List[int] or False:
    '''Solves the sudoku board if solvable.

    Args:
        bd: list of values in a sudoku board organized by rows

    Returns:
        A list representing the solved board or False if not solvable
    '''

    return fn_for_bd(Board(bd, [bd], []))


def fn_for_bd(bd: Board) -> List[int] or False:  # !!! Change to class calls
    '''Solves the sudoku board if solvable.

    Args:
        bd: a sudoku board

    Returns:
        A list representing the solved board or False if not solvable
    '''

    while not is_solved(bd.board):
        if bd.board == []:
            if len(bd.path) == 0 or len(bd.path) == 1:
                print("This board cannot be solved.")
                return False
            print("backtracking...")
            bd.board, bd.path = bd.path[-2], bd.path[0:-1]
        next_boards(bd)
    return bd.board


def is_solved(bd: List[int]) -> bool:
    '''Checks if the board is solved(there are no 0s)

    Args:
        bd: list of values in a sudoku board organized by rows

    Returns:
        True if the board contains no 0s, False otherwise
    '''

    if bd == []:
        return False
    for row in bd:
        if 0 in row:
            return False
    print("The board is solved!")
    return True


def next_boards(bd: Board) -> Board:
    '''Produce next valid board at first empty grid space

    Args:
        bd: sudoku board

    Returns:
        next valid Board
    '''

    valid_boards = [board for board in
                    filter(is_valid, all_boards(bd.board))]
    if valid_boards == []:
        bd.board = []
        return bd
    else:
        bd.board = is_not_visited(valid_boards, bd.visited)
        if bd.board == []:
            return bd
        bd.path.append(bd.board)
        bd.visited.append(bd.board)
        return bd


def all_boards(bd: List[int]) -> List[int]:
    '''Produces list of all possible boards at first 0

    Args:
        bd: list of values in a sudoku board organized by rows

    Returns:
        list of all possible board arrangements at first 0
    '''

    empty_row, empty_item = find_empty(bd)
    next_boards = []

    for x in range(9):
        next_board = copy.deepcopy(bd)
        next_board[empty_row][empty_item] = x + 1
        next_boards.append(next_board)

    return next_boards


def find_empty(bd: List[int]) -> List[int]:
    '''Finds the location of the first 0

    Args:
        bd: list of values in a sudoku board organized by rows

    Returns:
        the location of the first 0 in bd as a list, where list[0] is the row number and list[1] is the position within the row
    '''

    location = []
    for row in range(len(bd)):
        if 0 in bd[row]:
            return location + [row] + [bd[row].index(0)]


def is_valid(bd: List[int]) -> bool:
    '''Checks if board is valid(no duplicates in row, column, or square)

    Args:
        bd: list of values in a sudoku board organized by rows

    Returns:
        True if the board is valid, False if it violates a rule
    '''

    return is_row_valid(bd) and is_column_valid(bd) and is_square_valid(bd)


def is_row_valid(bd: List[int]) -> bool:
    '''Checks if board has duplicate non-zero values in a row

    Args:
        bd: list of values in a sudoku board organized by rows

    Returns:
        True if there are no non-zero duplicates, False otherwise
    '''

    for row in bd:
        for value in row:
            if value == 0:
                pass
            elif row.count(value) > 1:
                return False
    return True


def is_column_valid(bd: List[int]) -> bool:
    '''Checks if board has duplicate non-zero values in a column

    Args:
        bd: list of values in a sudoku board organized by rows

    Returns:
        True if there are no non-zero duplicates, False otherwise
    '''
    return is_row_valid(make_columns(bd))


def make_columns(bd: List[int]) -> List[int]:
    '''Re-organizes bd from a list of rows into a list of columns

    Args:
        bd: list of values in a sudoku board organized by rows

    Returns:
        list of values in a sudoku board organized by columns
    '''

    return ([[row[item] for row in bd] for item in range(9)])


def is_square_valid(bd: List[int]) -> bool:
    '''Produce true if a number appears at most once in a square section

    Args:
        bd: list of values in a sudoku board organized by rows

    Returns:
        True if there are no duplicates in a square section, False otherwise
    '''

    return is_row_valid(make_squares(bd))


def make_squares(bd: List[int]) -> List[int]:
    '''Re-organize bd from a list of rows into a list of 3x3 boards

    Args:
        bd: list of values in a sudoku board organized by rows

    Returns:
        list of values in a sudoku board organized by 3x3 squares
    '''

    return [Board.square(bd, [0, 3], [0, 3]), Board.square(bd, [0, 3], [3, 6]),
            Board.square(bd, [0, 3], [6, 9]), Board.square(bd, [3, 6], [0, 3]),
            Board.square(bd, [3, 6], [3, 6]), Board.square(bd, [3, 6], [6, 9]),
            Board.square(bd, [6, 9], [0, 3]), Board.square(bd, [6, 9], [3, 6]),
            Board.square(bd, [6, 9], [6, 9])]


def is_not_visited(lobd: List[List[int]],
                   visited: List[List[int]]) -> List[int]:
    '''Filters out boards that have been visited already

    Args:
        lobd: list of valid sudoku board arrangements
        visited: list of sudoku board arrangments checked previously

    Returns:
        first unvisited valid sudoku board arrangement found
    '''

    for bd in lobd:
        if bd not in visited:
            return bd
    return []


'''

bd = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

solver(bd)

'''
