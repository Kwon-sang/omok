import re
from typing import List, Dict, Tuple
from modules import settings


def player_name() -> Dict[int, str]:
    namespace = {}
    player1 = input(settings.CMD_NAME_PLAYER1)
    player2 = input(settings.CMD_NAME_PLAYER2)
    namespace[0] = f'{player1} - {settings.MARK_PLAYER1}'
    namespace[1] = f'{player2} - {settings.MARK_PLAYER2}'
    return namespace


def place() -> Tuple[bool, Tuple[int, int]]:
    """
    Receive user's stone position input which has format 'Num1 Num2'.
     If it has right formatted, return (int, int) tuple, else empty tuple.
     and other return is Game-quit-flag to quit the game with player.
    :return:  game-quit flag(bool), Stone place indices(tuple).
    """
    value = input(settings.CMD_PLACE)
    quit_flag = False
    if value == settings.QUIT_KEY:
        quit_flag = True
    if re.match(r'^\d+\s\d+$', value):
        i, j = value.split()
        value = (int(i), int(j))
    else:
        value = ()

    return quit_flag, value
