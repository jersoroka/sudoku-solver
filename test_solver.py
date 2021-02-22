'''Unit tests for sudoku solver'''

import unittest
import solver
from solver import Board

# ---EXAMPLE BOARDS---

# ---UNSOLVED BOARDS---
bd1 = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
       [9, 6, 5, 3, 2, 7, 1, 4, 8],
       [3, 4, 1, 6, 8, 9, 7, 5, 2],
       [5, 9, 3, 4, 6, 8, 2, 7, 1],
       [4, 7, 2, 5, 1, 3, 6, 8, 9],
       [6, 1, 8, 9, 7, 2, 4, 3, 5],
       [7, 8, 6, 2, 3, 5, 9, 1, 4],
       [1, 5, 4, 7, 9, 6, 8, 2, 3],
       [2, 3, 9, 8, 4, 1, 5, 6, 0]]

bd2 = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
       [9, 6, 5, 3, 2, 7, 1, 4, 8],
       [3, 4, 1, 6, 8, 9, 7, 5, 2],
       [5, 9, 3, 4, 6, 8, 2, 7, 1],
       [4, 7, 2, 5, 1, 3, 6, 8, 9],
       [6, 1, 8, 9, 7, 2, 4, 3, 5],
       [7, 8, 6, 2, 3, 5, 0, 0, 0],
       [1, 5, 4, 7, 9, 6, 0, 0, 0],
       [2, 3, 9, 8, 4, 1, 0, 0, 0]]

bd3 = [[5, 1, 6, 8, 4, 9, 7, 3, 2],
       [3, 0, 7, 6, 0, 5, 0, 0, 0],
       [8, 0, 9, 7, 0, 0, 0, 6, 5],
       [1, 3, 5, 0, 6, 0, 9, 0, 7],
       [4, 7, 2, 5, 9, 1, 0, 0, 6],
       [9, 6, 8, 3, 7, 0, 0, 5, 0],
       [2, 5, 3, 1, 8, 6, 0, 7, 4],
       [6, 8, 4, 2, 0, 7, 0, 5, 0],
       [2, 5, 3, 1, 8, 6, 0, 7, 4],
       [6, 8, 4, 2, 0, 7, 5, 0, 0],
       [7, 9, 1, 0, 5, 0, 6, 0, 8]]

bd4 = [[8, 0, 0, 9, 3, 0, 0, 0, 2],
       [0, 0, 9, 0, 0, 0, 0, 4, 0],
       [7, 0, 2, 1, 0, 0, 9, 6, 0],
       [2, 0, 0, 0, 0, 0, 0, 9, 0],
       [0, 6, 0, 0, 0, 0, 0, 7, 0],
       [0, 7, 0, 0, 0, 6, 0, 0, 5],
       [0, 2, 7, 0, 0, 8, 4, 0, 6],
       [0, 3, 0, 0, 0, 0, 5, 0, 0],
       [5, 0, 0, 0, 6, 2, 0, 0, 8]]

bd5 = [[8, 1, 0, 9, 3, 0, 0, 0, 2],
       [0, 0, 9, 0, 0, 0, 0, 4, 0],
       [7, 0, 2, 1, 0, 0, 9, 6, 0],
       [2, 0, 0, 0, 0, 0, 0, 9, 0],
       [0, 6, 0, 0, 0, 0, 0, 7, 0],
       [0, 7, 0, 0, 0, 6, 0, 0, 5],
       [0, 2, 7, 0, 0, 8, 4, 0, 6],
       [0, 3, 0, 0, 0, 0, 5, 0, 0],
       [5, 0, 0, 0, 6, 2, 0, 0, 8]]

bd6 = [[8, 4, 0, 9, 3, 0, 0, 0, 2],
       [0, 0, 9, 0, 0, 0, 0, 4, 0],
       [7, 0, 2, 1, 0, 0, 9, 6, 0],
       [2, 0, 0, 0, 0, 0, 0, 9, 0],
       [0, 6, 0, 0, 0, 0, 0, 7, 0],
       [0, 7, 0, 0, 0, 6, 0, 0, 5],
       [0, 2, 7, 0, 0, 8, 4, 0, 6],
       [0, 3, 0, 0, 0, 0, 5, 0, 0],
       [5, 0, 0, 0, 6, 2, 0, 0, 8]]

bd7 = [[8, 5, 0, 9, 3, 0, 0, 0, 2],
       [0, 0, 9, 0, 0, 0, 0, 4, 0],
       [7, 0, 2, 1, 0, 0, 9, 6, 0],
       [2, 0, 0, 0, 0, 0, 0, 9, 0],
       [0, 6, 0, 0, 0, 0, 0, 7, 0],
       [0, 7, 0, 0, 0, 6, 0, 0, 5],
       [0, 2, 7, 0, 0, 8, 4, 0, 6],
       [0, 3, 0, 0, 0, 0, 5, 0, 0],
       [5, 0, 0, 0, 6, 2, 0, 0, 8]]

bd8 = [[8, 2, 0, 9, 3, 0, 0, 0, 2],
       [0, 0, 9, 0, 0, 0, 0, 4, 0],
       [7, 0, 2, 1, 0, 0, 9, 6, 0],
       [2, 0, 0, 0, 0, 0, 0, 9, 0],
       [0, 6, 0, 0, 0, 0, 0, 7, 0],
       [0, 7, 0, 0, 0, 6, 0, 0, 5],
       [0, 2, 7, 0, 0, 8, 4, 0, 6],
       [0, 3, 0, 0, 0, 0, 5, 0, 0],
       [5, 0, 0, 0, 6, 2, 0, 0, 8]]

bd9 = [[8, 3, 0, 9, 3, 0, 0, 0, 2],
       [0, 0, 9, 0, 0, 0, 0, 4, 0],
       [7, 0, 2, 1, 0, 0, 9, 6, 0],
       [2, 0, 0, 0, 0, 0, 0, 9, 0],
       [0, 6, 0, 0, 0, 0, 0, 7, 0],
       [0, 7, 0, 0, 0, 6, 0, 0, 5],
       [0, 2, 7, 0, 0, 8, 4, 0, 6],
       [0, 3, 0, 0, 0, 0, 5, 0, 0],
       [5, 0, 0, 0, 6, 2, 0, 0, 8]]

bd10 = [[8, 6, 0, 9, 3, 0, 0, 0, 2],
        [0, 0, 9, 0, 0, 0, 0, 4, 0],
        [7, 0, 2, 1, 0, 0, 9, 6, 0],
        [2, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 0, 7, 0],
        [0, 7, 0, 0, 0, 6, 0, 0, 5],
        [0, 2, 7, 0, 0, 8, 4, 0, 6],
        [0, 3, 0, 0, 0, 0, 5, 0, 0],
        [5, 0, 0, 0, 6, 2, 0, 0, 8]]

bd11 = [[8, 7, 0, 9, 3, 0, 0, 0, 2],
        [0, 0, 9, 0, 0, 0, 0, 4, 0],
        [7, 0, 2, 1, 0, 0, 9, 6, 0],
        [2, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 0, 7, 0],
        [0, 7, 0, 0, 0, 6, 0, 0, 5],
        [0, 2, 7, 0, 0, 8, 4, 0, 6],
        [0, 3, 0, 0, 0, 0, 5, 0, 0],
        [5, 0, 0, 0, 6, 2, 0, 0, 8]]

bd12 = [[8, 8, 0, 9, 3, 0, 0, 0, 2],
        [0, 0, 9, 0, 0, 0, 0, 4, 0],
        [7, 0, 2, 1, 0, 0, 9, 6, 0],
        [2, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 0, 7, 0],
        [0, 7, 0, 0, 0, 6, 0, 0, 5],
        [0, 2, 7, 0, 0, 8, 4, 0, 6],
        [0, 3, 0, 0, 0, 0, 5, 0, 0],
        [5, 0, 0, 0, 6, 2, 0, 0, 8]]

bd13 = [[8, 9, 0, 9, 3, 0, 0, 0, 2],
        [0, 0, 9, 0, 0, 0, 0, 4, 0],
        [7, 0, 2, 1, 0, 0, 9, 6, 0],
        [2, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 0, 7, 0],
        [0, 7, 0, 0, 0, 6, 0, 0, 5],
        [0, 2, 7, 0, 0, 8, 4, 0, 6],
        [0, 3, 0, 0, 0, 0, 5, 0, 0],
        [5, 0, 0, 0, 6, 2, 0, 0, 8]]

# ---SOLVED BOARDS---

sbd1 = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
        [9, 6, 5, 3, 2, 7, 1, 4, 8],
        [3, 4, 1, 6, 8, 9, 7, 5, 2],
        [5, 9, 3, 4, 6, 8, 2, 7, 1],
        [4, 7, 2, 5, 1, 3, 6, 8, 9],
        [6, 1, 8, 9, 7, 2, 4, 3, 5],
        [7, 8, 6, 2, 3, 5, 9, 1, 4],
        [1, 5, 4, 7, 9, 6, 8, 2, 3],
        [2, 3, 9, 8, 4, 1, 5, 6, 7]]

sbd2 = [[8, 4, 6, 9, 3, 7, 1, 5, 2],
        [3, 1, 9, 6, 2, 5, 8, 4, 7],
        [7, 5, 2, 1, 8, 4, 9, 6, 3],
        [2, 8, 5, 7, 1, 3, 6, 9, 4],
        [4, 6, 3, 8, 5, 9, 2, 7, 1],
        [9, 7, 1, 2, 4, 6, 3, 8, 5],
        [1, 2, 7, 5, 9, 8, 4, 3, 6],
        [6, 3, 8, 4, 7, 1, 5, 2, 9],
        [5, 9, 4, 3, 6, 2, 7, 1, 8]]

# ---UNSOLVABLE BOARDS---

ibd1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

ibd2 = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

ibd3 = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# ---EXAMPLE INSTANCES---

bd1_instance = Board(bd1, [bd1], [])
bd4_instance = Board(bd4, [bd4], [])
next_bd1_instance = Board(sbd1, [bd1, sbd1], [sbd1])
next_bd4_instance = Board(bd5, [bd4, bd5], [bd4])

# ---TESTS---


class TestSolver(unittest.TestCase):

    def test_solver(self):
        self.assertEqual(solver.solver(bd1), sbd1)
        self.assertEqual(solver.solver(bd2), sbd1)
        self.assertFalse(solver.solver(bd3))
        self.assertEqual(solver.solver(bd4), sbd2)

    def test_is_solved(self):
        self.assertTrue(solver.is_solved(sbd1))
        self.assertFalse(solver.is_solved(bd1))

    def test_next_boards(self):

        def __eq__(self, other):
            if not isinstance(other, Board):
                return False

            return (self.board == other.board and
                    self.path == other.path and
                    self.visited == other.visited)

        __eq__(solver.next_boards(bd1_instance), next_bd1_instance)
        __eq__(solver.next_boards(bd4_instance), next_bd4_instance)

    def test_all_boards(self):
        self.assertEqual(solver.all_boards(bd4), [bd5, bd8, bd9, bd6, bd7,
                                                  bd10, bd11, bd12, bd13])

    def test_find_empty(self):
        self.assertEqual(solver.find_empty(bd1), [8, 8])
        self.assertEqual(solver.find_empty(bd2), [6, 6])
        self.assertEqual(solver.find_empty(bd3), [1, 1])

    def test_is_valid(self):
        self.assertTrue(solver.is_valid(bd5))
        self.assertFalse(solver.is_valid(bd8))
        self.assertFalse(solver.is_valid(bd9))
        self.assertTrue(solver.is_valid(bd6))
        self.assertFalse(solver.is_valid(ibd1))
        self.assertFalse(solver.is_valid(ibd2))
        self.assertFalse(solver.is_valid(ibd3))

    def test_is_row_valid(self):
        self.assertFalse(solver.is_row_valid(ibd1))
        self.assertTrue(solver.is_row_valid(bd5))
        self.assertTrue(solver.is_row_valid(ibd2))
        self.assertTrue(solver.is_row_valid(ibd3))

    def test_is_column_valid(self):
        self.assertTrue(solver.is_column_valid(bd5))
        self.assertTrue(solver.is_column_valid(ibd1))
        self.assertFalse(solver.is_column_valid(ibd2))
        self.assertTrue(solver.is_column_valid(ibd3))

    def test_is_square_valid(self):
        self.assertTrue(solver.is_square_valid(bd5))
        self.assertTrue(solver.is_square_valid(ibd1))
        self.assertTrue(solver.is_square_valid(ibd2))
        self.assertFalse(solver.is_square_valid(ibd3))


if __name__ == "__main__":
    unittest.main()
