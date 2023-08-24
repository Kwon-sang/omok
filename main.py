import os
from itertools import cycle
from modules.board import Board
from modules import commands, settings


def run():
    os.system(command='cls')
    print(settings.MSG_GAME_START)

    board = Board()
    players = commands.player_name()
    player_sequence = cycle(players.keys())

    # Loop for turn in game
    while True:
        os.system(command='cls')
        player_id = next(player_sequence)
        board.show()

        # Player put the stone. If that place is invalid, repeat util valid
        print(f'Player : {players.get(player_id)}')
        while True:
            quit_flag, place = commands.place()
            if quit_flag:
                return print(settings.MSG_QUIT)
            if (not place) or (not board.is_valid_place(place)):
                print(settings.ERROR_PLACE)
                continue
            board.set_place(place)
            break
        board.put(player_id)
        board.show()

        # Validate 'Omok' state. if satisfied, the game is over
        if board.is_omok():
            os.system(command='cls')
            board.show()
            return print(f"\nPlayer '{players[player_id]}' is Win!!")


if __name__ == '__main__':
    run()
