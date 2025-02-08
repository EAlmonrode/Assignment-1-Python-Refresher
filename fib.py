import time
from functools import lru_cache

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Finished in {end_time - start_time:.10f}s: {func.__name__}({args[0]}) -> {result}")
        return result
    return wrapper

@lru_cache(maxsize=None)
@timer
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    fib(100)