import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("{} time costs: {:.3f} seconds".format(func.__name__, end_time - start_time))
        return result
    return wrapper