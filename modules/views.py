import os

from modules.board import Board
from modules.settings import *


def start_view():
    os.system(command='cls')
    print(MSG_GAME_START)
    player1_name = input(CMD_NAME_PLAYER1)
    player2_name = input(CMD_NAME_PLAYER2)
    Board.set_user(player1_name, player2_name)
    os.system(command='cls')


def stone_input_view(player_id):
    Board.show_board()
    print(f"플레이어 : {Board.players.get(player_id)[0]}, 바둑돌 : {Board.players.get(player_id)[1]}")
    place_input_str = input(CMD_PLACE)
    try:
        Board.set_place(player_id, place_input_str)
    except ValueError as e:
        os.system(command='cls')
        print(e)
        stone_input_view(player_id)
    os.system(command='cls')
