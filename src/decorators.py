from functools import wraps


def repeatable(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
            except ValueError:
                continue
            else:
                return result
    return wrapper
