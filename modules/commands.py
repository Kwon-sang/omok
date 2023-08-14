from typing import List, Dict, Tuple
from modules import validations
from modules.settings import *


def input_player_name() -> Dict[int, str]:
    namespace = {}
    player1 = input(CMD_NAME_PLAYER1)
    player2 = input(CMD_NAME_PLAYER2)
    namespace[0] = f'{player1} - {MARK_PLAYER1}'
    namespace[1] = f'{player2} - {MARK_PLAYER2}'
    return namespace


def input_board_size() -> int:
    value = input(CMD_BOARD_SIZE)
    if validations.is_valid_board_size(value):
        return int(value)
    else:
        print(ERROR_BOARD_SIZE)
        return input_board_size()


def input_place(board: List[List[str]]) -> Tuple[int, int] or None:
    value = input(CMD_PLACE)
    if value == 'q' or value == 'Q':
        return

    if validations.is_valid_place(board, value):
        i, j = value.split()
        return int(i), int(j)
    else:
        print(ERROR_PLACE)
        return input_place(board)
