import re
from typing import List, Tuple
from modules import settings


def is_valid_board_size(size: str) -> bool:
    if not is_num(size):
        return False
    if int(size) < 5 or int(size) > 19:
        return False
    return True


def is_valid_place(board: List[List[str]], place: str) -> bool:
    size = len(board)
    if not re.match('^\d+\s\d+$', place):
        return False
    i, j = map(int, place.split())
    if min(i, j) < 0 or max(i, j) >= size:
        return False
    if board[i][j] != settings.MARK_GRID:
        return False
    return True


def is_num(target: str) -> object:
    return re.match('^\d+$', target)
