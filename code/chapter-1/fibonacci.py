from typing import Dict, Generator
from functools import lru_cache
import time
start_time = time.time()

# 1 - Infinite recursion
def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


# 2 - Recursive with base case
def fib2(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib2(n - 2) + fib2(n - 1)  # recursive case


# 3 - Memoization - store results as you create them to reuse later.
memo: Dict[int, int] = {0: 0, 1: 1}  # our base cases

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # memoization
    return memo[n]

# 4 - Automatic memoization with lru_cache decorator
# NOTE: lru_cache seems limited to fib(996)
@lru_cache()
def fib4(n: int) -> int:  # same definition as fib2()
    if n < 2:  # base case
        return n
    return fib4(n - 2) + fib4(n - 1)  # recursive case


# 5 - simple iterative approach
def fib5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next  # tuple unpacking
    return next

# 6 - using a generator
def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0: yield 1  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next  # tuple unpacking
        yield next  # main generation step


if __name__ == "__main__":
    for i in range(10000):
        fib3(10)
    print("Time taken:", time.time() - start_time)
