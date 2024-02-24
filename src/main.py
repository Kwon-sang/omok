import os
import itertools
import user_input
import settings
from board import Board


def run() -> bool:
    """One-shot game logic.

    This function is one-shot game of Omok.
    If any user complete Omok, the user is given options whether exit or resume.
    Return state depends on that user's choices.
    """
    os.system(command='cls')
    board = Board(input_size=user_input.size, input_users=user_input.username)
    user_cycle = itertools.cycle(board.users.values())

    while True:
        os.system(command='cls')
        print(board)
        user_name, user_mark = next(user_cycle)
        print(settings.INFO_CURRENT_USER.format(user_name, user_mark))
        board.set_position(user_name, input_position=user_input.position)
        if board.is_omok():
            print(settings.INFO_COMPLETE.format(user_name))
            return user_input.re_game()


# Main logic - make repeated game.
while True:
    flag = run()
    if not flag:
        raise SystemExit(settings.INFO_EXIT)
