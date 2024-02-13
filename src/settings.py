MARK_EMPTY = '·'
MARK_USER1 = '●'
MARK_USER2 = '○'
QUIT_KEY = 'Q'

INPUT_SIZE = "\033[36m" + "바둑판 크기를 입력하세요(5이상, 30이하) : " + "\033[0m"
INPUT_POSITION = "\033[36m" + "위치를 입력하세요(종료 커맨드-Q) : " + "\033[0m"
INPUT_RE_GAME = "게임을 재시작 하시겠습니까? [Y/N]"

ERROR_NAME_CONFLICT = "\033[91m" + "사용자1의 이름과 사용자2의 이름은 동일할 수 없습니다. 다시 입력해 주세요." + "\033[0m"
ERROR_INVALID_FORMAT = "\033[91m" + "올바르지 않은 입력 형식 입니다." + "\033[0m"
ERROR_INVALID_RANGE = "\033[91m" + "올바르지 않은 입력 범위 입니다." + "\033[0m"
ERROR_INVALID_POSITION = "\033[91m" + "올바르지 않은 위치 입니다." + "\033[0m"

INFO_COMPLETE = "{} \033[92m" + "승리!!" + "\033[0m"
INFO_CURRENT_USER = "\033[92m" + "[현재 유저 턴 : {}, 바둑돌 : {}]" + "\033[0m"
INFO_EXIT = "게임을 종료 합니다."
