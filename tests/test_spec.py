import unittest
from src.game import ConnectFour


class ConnectFourTest(unittest.TestCase):
    def test_victory_1(self):

        file = "board_1"
        board = [[], [], [], [], [], []]
        test = open(file, "r")
        game_board = test.readlines()

        rows = 0
        for _ in game_board:
            for num in game_board[rows]:
                if num != '\n':
                    board[rows].append(int(num))
                else:
                    rows += 1

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_2(self):

        file = "board_2"
        board = [[], [], [], [], [], []]
        test = open(file, "r")
        game_board = test.readlines()

        rows = 0
        for _ in game_board:
            for num in game_board[rows]:
                if num != '\n':
                    board[rows].append(int(num))
                else:
                    rows += 1

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_3(self):

        file = "board_3"
        board = [[], [], [], [], [], []]
        test = open(file, "r")
        game_board = test.readlines()

        rows = 0
        for _ in game_board:
            for num in game_board[rows]:
                if num != '\n':
                    board[rows].append(int(num))
                else:
                    rows += 1

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_4(self):

        file = "board_4"
        board = [[], [], [], [], [], []]
        test = open(file, "r")
        game_board = test.readlines()

        rows = 0
        for _ in game_board:
            for num in game_board[rows]:
                if num != '\n':
                    board[rows].append(int(num))
                else:
                    rows += 1
        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_5(self):

        file = "board_5"
        board = [[], [], [], [], [], []]
        test = open(file, "r")
        game_board = test.readlines()

        rows = 0
        for _ in game_board:
            for num in game_board[rows]:
                if num != '\n':
                    board[rows].append(int(num))
                else:
                    rows += 1

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_6(self):

        file = "board_6"
        board = [[], [], [], [], [], []]
        test = open(file, "r")
        game_board = test.readlines()

        rows = 0
        for _ in game_board:
            for num in game_board[rows]:
                if num != '\n':
                    board[rows].append(int(num))
                else:
                    rows += 1

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_7(self):

        file = "board_7"
        board = [[], [], [], [], [], []]
        test = open(file, "r")
        game_board = test.readlines()

        rows = 0
        for _ in game_board:
            for num in game_board[rows]:
                if num != '\n':
                    board[rows].append(int(num))
                else:
                    rows += 1

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_8(self):

        file = "board_8"
        board = [[], [], [], [], [], []]
        test = open(file, "r")
        game_board = test.readlines()

        rows = 0
        for _ in game_board:
            for num in game_board[rows]:
                if num != '\n':
                    board[rows].append(int(num))
                else:
                    rows += 1

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_9(self):

        file = "board_9"
        board = [[], [], [], [], [], []]
        test = open(file, "r")
        game_board = test.readlines()

        rows = 0
        for _ in game_board:
            for num in game_board[rows]:
                if num != '\n':
                    board[rows].append(int(num))
                else:
                    rows += 1

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_victory_10(self):

        file = "board_10"
        board = [[], [], [], [], [], []]
        test = open(file, "r")
        game_board = test.readlines()

        rows = 0
        for _ in game_board:
            for num in game_board[rows]:
                if num != '\n':
                    board[rows].append(int(num))
                else:
                    rows += 1

        player = [0, 1]

        win = ConnectFour.victory(board, player)

        expected_outcome = 1

        self.assertEqual(win, expected_outcome)

    def test_player_turn(self):

        test_player_1 = 1
        test_player_2 = 2

        game = ConnectFour()

        board = game.player_turn(test_player_1, 1)

        self.assertEqual(board[0][0], test_player_1)

        board = game.player_turn(test_player_2, 1)

        self.assertEqual((board[1][0]), test_player_2)

        board = game.player_turn(test_player_1, 2)

        self.assertEqual(board[0][1], test_player_1)

        board = game.player_turn(test_player_2, 2)

        self.assertEqual((board[1][1]), test_player_2)


if __name__ == '__main__':
    unittest.main()

