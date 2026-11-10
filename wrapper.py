import time
from functools import wraps

def execution_timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        finally:
            end = time.perf_counter()
            print(f"{func.__name__} took {end-start} seconds")
        return result
    return inner

@execution_timer
def calculate_sum(n):
    return sum(range(n))


@execution_timer
def find_factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


@execution_timer
def greet(name, message="Hello"):
    return f"{message}, {name}!"




print(calculate_sum(1_000_000))
print(find_factorial(1000))
print(greet("Samuel", message="Welcome"))