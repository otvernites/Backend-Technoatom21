import numpy as np
from exceptions import ValueTooLargeError, ZeroValueError, SizeError, ChoiceError


class TicTacGame:
    def __init__(self, first_name="Player1", second_name="Player2", size=1):
        self.size = size
        self.first_name = first_name
        self.second_name = second_name
        self.board = np.full((size, size), " ")

    def show_board(self):
        count = self.size
        for i in range(count):
            print('+' + count * ('-' * 7 + '+'))
            board_str = np.array2string(self.board[i], precision=1, separator='  |  ')
            print('|  ' + board_str[1:-1] + '  |')
        print('+' + count * ('-' * 7 + '+'))

    def validate_input_name(self, name, num):
        count = 15
        if num < 1 or num > 2:
            raise IndexError
        if len(name) > count:
            raise ValueTooLargeError
        if len(name) == 0:
            raise ZeroValueError
        if num == 1:
            self.first_name = name
        else:
            self.second_name = name

    def validate_input_size(self, size):
        dim = 0
        try:
            dim = int(size)
        except ValueError:
            pass
        if dim <= 1 or dim > 10:
            raise SizeError
        self.board = np.resize(self.board, (dim, dim))
        self.size = dim

    def validate_move(self, coord, sign):
        if (coord[0] < 0 or coord[0] > self.size) or (coord[1] < 0 or coord[1] > self.size):
            raise IndexError
        if not self.board[coord[0]][coord[1]] == " ":
            raise ChoiceError

        if sign == 0:
            print(self.board[coord[0]][coord[1]])
            self.board[coord[0]][coord[1]] = "X"
        else:
            self.board[coord[0]][coord[1]] = "0"

    def start_game(self):
        while True:
            try:
                name1 = input("Enter the first username: ")
                self.validate_input_name(name1, 1)
                break
            except ValueTooLargeError:
                print("A very long name! Enter a new username.")
            except ZeroValueError:
                print("You haven't entered anything. Try again.")

        while True:
            try:
                name2 = input("Enter the second username: ")
                self.validate_input_name(name2, 2)
                break
            except ValueTooLargeError:
                print("A very long name! Enter a new username.")
            except ZeroValueError:
                print("You haven't entered anything. Try again.")

        while True:
            try:
                size = input("Enter the length of the field: ")
                self.validate_input_size(size)
                break
            except ValueError:
                print("Enter the number.")
            except SizeError:
                print("Wrong size. Try again!")
        self.game()

    def game(self):
        for i in range(self.size ** 2 + 1):
            self.show_board()
            res = self.check_winner()
            if res == 0:
                if i % 2 == 0:
                    print(self.first_name + "'s move: ")
                    sign = 0
                else:
                    print(self.second_name + "'s move: ")
                    sign = 1
                while True:
                    try:
                        print("! Please enter 2 numbers via comma: row,col ! ")
                        coord = tuple(map(int, input(' ').split(",")))
                        self.validate_move(coord, sign)
                        break
                    except ValueError:
                        print("Enter the number.")
                    except IndexError:
                        print("The index is out of bounds. Try again!")
                    except ChoiceError:
                        print("This cell is already filled. Try again!")
            elif res == 1:
                print(self.first_name + " won!")
                return
            elif res == 2:
                print(self.second_name + " won!")
                return
        print("Ничья!")

    def check_winner(self):
        result = 0
        test = np.full((self.size, self.size), " ")
        if np.array_equal(test, self.board):
            return result
        for i in range(self.size):
            if np.all((self.board[i, :] == "X")) or np.all((self.board[:, i] == "X")) or \
                    np.all((self.board.diagonal() == "X")):
                result = 1
                return result
            if np.all((self.board[i, :] == "0")) or np.all((self.board[:, i] == "0")) or \
                    np.all((self.board.diagonal() == "0")):
                result = 2
                return result
        return result


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
    input()
