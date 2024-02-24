from functools import wraps


def repeatable(func):
    """If decorated function raise Error, make resume the decorated function again."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
            except ValueError as e:
                print(e)
                continue
            else:
                return result
    return wrapper
