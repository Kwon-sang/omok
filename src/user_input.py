import re


def board_size() -> int:
    size_input = input("바둑판 크기를 입력하세요 : ")
    if not re.match('^[0-9]+$', size_input):
        raise ValueError("Invalid input")
    return int(size_input)


def username() -> dict:
    user1 = input("사용자1 이름 : ")
    user2 = input("사용자1 이름 : ")
    if user1 == user2:
        raise ValueError("Invalid input")
    return {"user1": user1, "user2": user2}


def position() -> tuple[int, int]:
    position_input = input("위치를 입력하세요(종료 커맨드-Q) : ")
    if position_input == 'Q':
        raise SystemExit("게임을 종료 합니다.")
    if not re.match('^[0-9]+\s[0-9]+$', position_input):
        raise ValueError("Invalid input")
    x, y = position_input.split()
    return int(x), int(y)
