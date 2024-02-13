import settings

from decorators import repeatable


class Board:

    latest_position = None

    def __init__(self, input_size, input_users):
        if not callable(input_size) or not callable(input_users):
            raise TypeError
        self.size: int = input_size()
        self.users: dict = input_users()
        self.board = [[settings.MARK_EMPTY] * self.size for _ in range(self.size)]

    @repeatable
    def set_position(self, user: str, input_position) -> None:
        if not callable(input_position):
            raise TypeError
        position = input_position()
        self._is_valid_position(position)
        self.latest_position = position
        x, y = position
        if user in self.users.get("user1"):
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

        result = ''
        for i in index_board:
            result += ' '.join(i)
            result += '\n'
        return result

    def _is_valid_position(self, position: tuple):
        x, y = position
        if x >= self.size or y >= self.size:
            raise ValueError(settings.ERROR_INVALID_RANGE)
        if self.board[y][x] != settings.MARK_EMPTY:
            raise ValueError(settings.ERROR_INVALID_POSITION)

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
