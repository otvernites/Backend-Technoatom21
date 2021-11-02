import unittest
import numpy as np
from exceptions import *
from main import TicTacGame


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()

    def test_init(self):
        player1 = "Player1"
        player2 = "Player2"
        self.assertEqual(self.game.first_name, player1)
        self.assertEqual(self.game.second_name, player2)

    def test_validate_input_name(self):
        self.game.validate_input_name("Masha", 1)
        self.assertEqual(self.game.first_name, "Masha")

        with self.assertRaises(IndexError):
            self.game.validate_input_name("Masha", 4)

        with self.assertRaises(ValueTooLargeError):
            self.game.validate_input_name("Alexander Alexandrovich Samuilov", 2)

        with self.assertRaises(ZeroValueError):
            self.game.validate_input_name("", 2)

    def test_validate_input_size(self):
        self.game.validate_input_size("3")
        self.assertEqual(self.game.size, 3)

        with self.assertRaises(SizeError):
            self.game.validate_input_size("100")

        with self.assertRaises(SizeError):
            self.game.validate_input_size("0")

    def test_validate_move(self):
        self.game = TicTacGame("p1", "p2", 3)

        with self.assertRaises(IndexError):
            self.game.validate_move((100, 1), 0)

        with self.assertRaises(IndexError):
            self.game.validate_move((-1, 1), 1)

        with self.assertRaises(IndexError):
            self.game.validate_move((3, 1), 0)

        self.game.validate_move((0, 0), 0)
        self.assertEqual(self.game.board[0, 0], 'X')

        self.game.validate_move((0, 1), 1)
        self.assertEqual(self.game.board[0, 1], '0')

        with self.assertRaises(ChoiceError):
            self.game.validate_move((0, 0), 1)

    def test_check_winner(self):
        self.game = TicTacGame("p1", "p2", 2)
        self.game.board = np.array([['X', 'X'], ['0', ' ']])
        self.assertEqual(self.game.check_winner(), 1)

        self.game.validate_input_size("3")
        self.game.board = np.array([['0', '0', 'X'], ['X', '0', '0'], ['X', '0', 'X']])
        self.assertEqual(self.game.check_winner(), 2)

        self.game.validate_input_size("3")
        self.game.board = np.array([[' ', 'X', '0'], ['X', 'X', 'X'], ['0', ' ', '0']])
        self.assertEqual(self.game.check_winner(), 1)

        self.game.board = np.array([['X', 'X', '0'], ['0', 'X', 'X'], ['X', '0', '0']])
        self.assertEqual(self.game.check_winner(), 0)

if __name__ == '__main__':
    unittest.main()
