from typing import List, Tuple
from modules.settings import *


def create(size: int) -> List[List[str]]:
    return [[MARK_GRID] * size for _ in range(size)]


def put(board: List[List[str]],
        player_id: int,
        place: Tuple[int, int]) -> Tuple[int, int]:
    if player_id == 0:
        board[place[0]][place[1]] = MARK_PLAYER1
    else:
        board[place[0]][place[1]] = MARK_PLAYER2
    return place


def show(board: List[List[str]]) -> None:
    board_size = len(board)
    index_board = [['0'] * (board_size+1) for _ in range(board_size+1)]
    index_board[0][0] = '.'
    for i in range(board_size):
        index_board[0][i+1] = f'{i:2d}'
        index_board[i+1][0] = f'{i:2d}'
    for i in range(board_size):
        for j in range(board_size):
            index_board[i+1][j+1] = f'{board[i][j]:2s}'
    for i in index_board:
        print(' '.join(i))


def is_omok(board: List[List[str]], place: Tuple[int, int] = None) -> bool:
    if place is None:
        return False

    d1 = [1, 0, 1, 1]
    d2 = [0, 1, 1, -1]
    for i in range(4):
        count = 1
        for j in range(1, 5):
            next_place1 = (place[0] + d1[i]*j, place[1] + d2[i]*j)  # the direction of right
            next_place2 = (place[0] - d1[i]*j, place[1] - d2[i]*j)  # the direction of reverse
            if __is_valid(board, place, next_place1):
                count += 1
            if __is_valid(board, place, next_place2):
                count += 1
        if count >= 5:
            return True
    return False


def __is_valid(board: List[List[str]],
               origin_place: Tuple[int, int],
               next_place: Tuple[int, int]) -> bool:
    board_size = len(board)
    i, j = origin_place
    next_i, next_j = next_place
    if (0 <= max(next_i, next_j) < board_size) and (board[i][j] == board[next_i][next_j]):
        return True
    return False
