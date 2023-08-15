import os
from itertools import cycle
from modules import commands, boards
from modules.settings import *


def run():
    os.system(command='cls')
    print(MSG_GAME_START)
    players = commands.input_player_name()
    board_size = commands.input_board_size()
    board = boards.create(board_size)
    player_order = cycle(players.keys())
    player_id = None
    place = None
    while not boards.is_omok(board, place):
        os.system(command='cls')
        player_id = next(player_order)
        boards.show(board)
        print(f'\nplayer : {players.get(player_id)}')
        place = commands.input_place(board)
        if place is None:
            print(MSG_QUIT)
            return
        else:
            boards.put(board, player_id, place)
            boards.show(board)

    os.system(command='cls')
    boards.show(board)
    print(f"\nPlayer '{players[player_id]}' is Win!!")


if __name__ == '__main__':
    run()
