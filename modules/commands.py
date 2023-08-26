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


def place() -> Tuple[int, int]:
    """
    Receive user's stone position input which has format 'Num1 Num2'.

    :raise: Exception - when input value is 'Q'
            ValueError - when input value is invalid format
    """
    value = input(settings.CMD_PLACE)
    if value == settings.QUIT_KEY:
        return settings.QUIT_KEY
    if not re.match(r'^\d+\s\d+$', value):
        raise ValueError()
    i, j = map(int, value.split())
    return i, j
