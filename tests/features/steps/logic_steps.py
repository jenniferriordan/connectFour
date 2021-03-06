from behave import *
from src.game import ConnectFour


@given("The board is initialized")
def step_the_board_is_initialized(context):

    board = ConnectFour().player_turn()

    return board


@given("The board contains only zeros")
def step_the_board_contains_only_zeros(context):

    board = step_the_board_is_initialized(context)

    non_zeros = []
    for row in board:
        for num in row:
            if num != 0:
                non_zeros.append(num)

    expected_length = 0

    assert len(non_zeros) is expected_length




