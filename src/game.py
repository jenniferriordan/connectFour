import numpy


class ConnectFour:

    def __init__(self):

        self.game_matrix = [[0 for x in range(7)] for y in range(6)]
        self.player_one = 21
        self.player_two = 21
        self.p1_game_piece = 1
        self.p2_game_piece = 2

    def player(self, one=None, two=None):

        if one:
            return [self.player_one, self.p1_game_piece]
        else:
            return [self.player_two, self.p2_game_piece]

    @staticmethod
    def victory(game_board, player):

        winner = player[1]

        rows = 0

        for _ in game_board:

            for i, num in enumerate(game_board[rows]):

                # Vertical
                if rows < 3 and num == player[1]:
                    if game_board[rows][i] == player[1] and game_board[rows + 1][i] == player[1] \
                         and game_board[rows + 2][i] == player[1] and game_board[rows + 3][i] == player[1]:
                            return winner

                # Horizontal
                if i < 4 and num == player[1]:
                    if game_board[rows][i] == player[1] and game_board[rows][i + 1] == player[1] \
                         and game_board[rows][i + 2] == player[1] and game_board[rows][i + 3] == player[1]:
                            return winner

                # Positive
                # Diagonal
                if rows < 3 and i < 4 and num == player[1]:
                    if game_board[rows][i] == player[1] and game_board[rows + 1][i + 1] == player[1] \
                         and game_board[rows + 2][i + 2] == player[1] and game_board[rows + 3][i + 3] == player[1]:
                            return winner

                # Negative
                # Diagonal
                if rows < 3 and i > 2 and num == player[1]:
                    if game_board[rows][i] == player[1] and game_board[rows + 1][i - 1] == player[1] \
                         and game_board[rows + 2][i - 2] == player[1] and game_board[rows + 3][i - 3] == player[1]:
                            return winner

                # Move search to the next row
                if i == 6:
                    i = 0
                    rows += 1

    def player_move(self, player, move):

        if player == 1:
            player = ConnectFour.player(self, one=player)
        else:
            player = ConnectFour.player(self, two=player)

        game_board = self.game_matrix

        i = 0
        while i < 7:
            if player[0] > 0:
                if game_board[i][move - 1] == 0:
                    game_board[i][move - 1] = player[1]
                    player[0] = player[0] - 1
                    break
                else:
                    i += 1

        win = ConnectFour.victory(game_board, player)

        if win:
            return win
        else:
            return game_board






