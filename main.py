from modules import views
from modules.board import Board


def run():
    views.start_view()
    while True:
        views.stone_input_view(player_id=Board.current_player)
        if Board.is_omok():
            Board.show_board()
            player_name = Board.players.get(Board.current_player)[0]
            player_stone = Board.players.get(Board.current_player)[1]
            print(f"[Win!!!] {player_name}({player_stone}) 님이 오목을 달셩하였습니다.")
            quit()
        Board.switch_player()


if __name__ == '__main__':
    run()
