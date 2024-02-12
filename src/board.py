import settings

from decorators import repeatable


class Board:

    latest_position = None

    def __init__(self, size: int, users: dict):
        self.size: int = size
        self.users: dict = users
        self.board = [[settings.MARK_EMPTY] * size for _ in range(size)]

    @repeatable
    def set_position(self, user: str, position: tuple) -> None:
        self._is_valid_position(position)
        self.latest_position = position
        x, y = position
        if self.users.get("user1") == user:
            self.board[y][x] = settings.MARK_USER1
        else:
            self.board[y][x] = settings.MARK_USER2

    def __str__(self):
        index_board = [['0'] * (self.size + 1) for _ in range(self.size + 1)]
        index_board[0][0] = '.'

        for i in range(self.size):
            index_board[0][i+1] = f'{i:2d}'
            index_board[i+1][0] = f'{i:2d}'
        for i in range(self.size):
            for j in range(self.size):
                index_board[i+1][j+1] = f'{self.board[i][j]:2s}'
        for i in index_board:
            print(' '.join(i))

    def _is_valid_position(self, position: tuple):
        x, y = position
        if self.board[y][x] != settings.MARK_EMPTY:
            raise ValueError

    def is_omok(self) -> bool:
        x, y = self.latest_position
        if self.board[y][x] == settings.MARK_EMPTY:
            return False
        d1 = [1, 0, 1, 1]   # Directions X
        d2 = [0, 1, 1, -1]  # Directions Y
        for i in range(4):
            count = 1
            for j in range(1, 5):
                nx1 = x + d1[i]*j  # Next X position(forward direction)
                nx2 = x - d1[i]*j  # Next Y position(forward direction)
                ny1 = y + d2[i]*j  # Next X position(reversed direction)
                ny2 = y - d2[i]*j  # Next Y position(reversed direction)
                if (min(nx1, ny1) >= 0 and max(nx1, ny1) < self.size) and (self.board[y][x] == self.board[ny1][nx1]):
                    count += 1
                if (min(nx2, ny2) >= 0 and max(nx2, ny2) < self.size) and (self.board[y][x] == self.board[ny2][nx2]):
                    count += 1
            if count >= 5:
                return True
        return False
