import os
import itertools
from typing import Tuple

from modules.board import Board
from modules import commands, settings


def run():
    os.system(command='cls')
    print(settings.MSG_GAME_START)
    board = Board()
    players = commands.player_name()
    player_sequence = itertools.cycle(players.keys())

    # Loop for turn in game
    while not board.is_omok():
        os.system(command='cls')
        player_id = next(player_sequence)
        board.show()
        # Player put the stone. If that place is invalid, repeat util valid
        print(f'Player : {players.get(player_id)}')
        place = ''
        while True:
            try:
                place = commands.place()
            except ValueError:
                print(settings.ERROR_PLACE)
                continue
            if place == settings.QUIT_KEY:
                print(settings.MSG_QUIT)
                return
            if board.is_valid_place(place):
                break
            else:
                print(settings.ERROR_PLACE)
                continue
        board.set_place(place)
        board.put(player_id)
        board.show()
    os.system(command='cls')
    board.show()
    return print(f"\nPlayer '{players[player_id]}' is Win!!")


if __name__ == '__main__':
    run()
