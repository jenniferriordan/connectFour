import unittest
from src.game import ConnectFour


class ConnectFourTest(unittest.TestCase):

    @staticmethod
    def read_board(filename):

        board = [[], [], [], [], [], []]
        test = open(filename, "r")
        game_board = test.readlines()

        rows = 0
        for _ in game_board:
            for num in game_board[rows]:
                if num != '\n':
                    board[rows].append(int(num))
                else:
                    rows += 1

        test.close()
        return board

    def test_victory_1(self):

        file = "board_1"
        board = ConnectFourTest.read_board(file)

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_2(self):

        file = "board_2"
        board = ConnectFourTest.read_board(file)

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_3(self):

        file = "board_3"
        board = ConnectFourTest.read_board(file)

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_4(self):

        file = "board_4"
        board = ConnectFourTest.read_board(file)
        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_5(self):

        file = "board_5"
        board = ConnectFourTest.read_board(file)

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_6(self):

        file = "board_6"
        board = ConnectFourTest.read_board(file)

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_7(self):

        file = "board_7"
        board = ConnectFourTest.read_board(file)

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_8(self):

        file = "board_8"
        board = ConnectFourTest.read_board(file)

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_9(self):

        file = "board_9"
        board = ConnectFourTest.read_board(file)

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_10(self):

        file = "board_10"
        board = ConnectFourTest.read_board(file)

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

if __name__ == '__main__':
    unittest.main()

