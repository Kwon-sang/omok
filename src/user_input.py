import re
import settings
from decorators import repeatable


@repeatable
def size() -> int:
    size_input: str = input(settings.INPUT_SIZE)
    if not re.match('^[0-9]+$', size_input):
        raise ValueError(settings.ERROR_INVALID_FORMAT)
    size_input: int = int(size_input)
    if size_input < 5 or size_input > 30:
        raise ValueError(settings.ERROR_INVALID_RANGE)
    return size_input


@repeatable
def username() -> dict:
    user1 = input("사용자1 이름 : ")
    user2 = input("사용자2 이름 : ")
    if user1 == user2:
        raise ValueError(settings.ERROR_NAME_CONFLICT)
    return {
        "user1": (user1, settings.MARK_USER1),
        "user2": (user2, settings.MARK_USER2)
    }


@repeatable
def position() -> tuple[int, int]:
    position_input = input(settings.INPUT_POSITION)
    if position_input == settings.QUIT_KEY:
        raise SystemExit(settings.INFO_EXIT)
    if not re.match('^[0-9]+\s[0-9]+$', position_input):
        raise ValueError(settings.ERROR_INVALID_FORMAT)
    x, y = position_input.split()
    return int(x), int(y)


@repeatable
def re_game() -> bool:
    flag = input(settings.INPUT_RE_GAME)
    if not re.match("^[YN]$", flag):
        raise ValueError(settings.ERROR_INVALID_FORMAT)
    if flag == "Y":
        return True
    else:
        return False
