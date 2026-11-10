from functools import wraps

def logger(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"{func.__name__} is starting...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} has finished!")
        return result
    return inner

@logger
def add(a, b):
    return a + b


@logger
def greet(name):
    return f"Hello, {name}!"


@logger
def multiply(a, b, c):
    return a * b * c


print(add(5, 10))
print(greet("Samuel"))
print(multiply(2, 3, 4))