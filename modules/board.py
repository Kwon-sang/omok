import re

from modules.settings import *


class Board:
    players = {}
    current_player = 0
    _recent_place = (None, None)
    _board = [[MARK_GRID] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    @classmethod
    def set_user(cls, player1_name, player2_name):
        cls.players[0] = (player1_name, MARK_PLAYER1)
        cls.players[1] = (player2_name, MARK_PLAYER2)

    @classmethod
    def switch_player(cls):
        cls.current_player = (cls.current_player + 1) % 2

    @classmethod
    def set_place(cls, player_id, input_str):
        row, col = cls._user_place_parser(input_str)
        cls._recent_place = (row, col)
        cls._board[row][col] = MARK_PLAYER1 if player_id == 0 else MARK_PLAYER2

    @classmethod
    def _user_place_parser(cls, input_str: str):
        if input_str == QUIT_KEY:
            print(MSG_QUIT)
            quit()
        if not re.match(r'^\d+\s\d+$', input_str):
            raise ValueError(ERROR_FORMAT)
        row, col = map(int, input_str.split())
        if min(row, col) < 0 or max(row, col) >= BOARD_SIZE:
            raise ValueError(ERROR_PLACE_INVALID_RANGE)
        if cls._board[row][col] != MARK_GRID:
            raise ValueError(ERROR_PLACE_DUPLICATED)
        return row, col

    @classmethod
    def show_board(cls):
        index_board = [['0'] * (BOARD_SIZE+1) for _ in range(BOARD_SIZE+1)]
        index_board[0][0] = '.'
        for i in range(BOARD_SIZE):
            index_board[0][i+1] = f'{i:2d}'
            index_board[i+1][0] = f'{i:2d}'
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                index_board[i+1][j+1] = f'{cls._board[i][j]:2s}'
        for i in index_board:
            print(' '.join(i))

    @classmethod
    def is_omok(cls) -> bool:
        row, col = cls._recent_place
        if cls._board[row][col] == MARK_GRID:
            return False
        d1 = [1, 0, 1, 1]
        d2 = [0, 1, 1, -1]
        for i in range(4):
            count = 1
            for j in range(1, 5):
                next_place_forward = (row + d1[i]*j, col + d2[i]*j)  # the direction of right
                next_place_reverse = (row - d1[i]*j, col - d2[i]*j)  # the direction of reverse
                if min(next_place_forward) >= 0 and max(next_place_forward) < BOARD_SIZE \
                        and cls._is_mark_equal(cls._recent_place, next_place_forward):
                    count += 1
                if min(next_place_forward) >= 0 and max(next_place_forward) < BOARD_SIZE \
                        and cls._is_mark_equal(cls._recent_place, next_place_reverse):
                    count += 1
            if count >= 5:
                return True
        return False

    @classmethod
    def _is_mark_equal(cls, place1, place2):
        row1, col1 = place1
        row2, col2 = place2
        return cls._board[row1][col1] == cls._board[row2][col2]
