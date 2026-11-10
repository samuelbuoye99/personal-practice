cache = [0, 1]

def fib(n):
    if n<len(cache):
        return cache[n]
    result = fib(n-1) + fib(n-2)
    cache.append(result)
    return result

print(fib(10))