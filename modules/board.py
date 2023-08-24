from typing import List, Tuple
from modules import settings


class Board:
    def __init__(self):
        self.place = (0, 0)
        self.board_size = settings.board_size
        self.board = [[settings.MARK_GRID] * self.board_size for _ in range(self.board_size)]

    def set_place(self, place):
        self.place = place

    def put(self, player_id: int) -> Tuple[int, int]:
        row, col = self.place
        if player_id == 0:
            self.board[row][col] = settings.MARK_PLAYER1
        elif player_id == 1:
            self.board[row][col] = settings.MARK_PLAYER2
        return self.place

    def show(self) -> None:
        index_board = [['0'] * (self.board_size+1) for _ in range(self.board_size+1)]
        index_board[0][0] = '.'
        for i in range(self.board_size):
            index_board[0][i+1] = f'{i:2d}'
            index_board[i+1][0] = f'{i:2d}'
        for i in range(self.board_size):
            for j in range(self.board_size):
                index_board[i+1][j+1] = f'{self.board[i][j]:2s}'
        for i in index_board:
            print(' '.join(i))

    def is_omok(self) -> bool:
        row, col = self.place
        if self.board[row][col] == settings.MARK_GRID:
            return False
        d1 = [1, 0, 1, 1]
        d2 = [0, 1, 1, -1]
        for i in range(4):
            count = 1
            for j in range(1, 5):
                next_place_forward = (row + d1[i]*j, col + d2[i]*j)  # the direction of right
                next_place_reverse = (row - d1[i]*j, col - d2[i]*j)  # the direction of reverse
                if min(next_place_forward) >= 0 and max(next_place_forward) < self.board_size \
                        and self.is_mark_equal(self.place, next_place_forward):
                    count += 1
                if min(next_place_forward) >= 0 and max(next_place_forward) < self.board_size \
                        and self.is_mark_equal(self.place, next_place_reverse):
                    count += 1
            if count >= 5:
                return True
        return False

    def is_mark_equal(self, place1, place2):
        row1, col1 = place1
        row2, col2 = place2
        return self.board[row1][col1] == self.board[row2][col2]

    def is_valid_place(self, place: Tuple[int, int]) -> bool:
        row, col = place
        if min(row, col) < 0 or max(row, col) >= self.board_size:
            return False
        if self.board[row][col] != settings.MARK_GRID:
            return False
        return True
