from typing import Dict

# Attempt 1 - Infinite recursion
def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


# Attempt 2 - recusrive with base case
def fib2(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib2(n - 2) + fib2(n - 1)  # recursive case


# Memoization - store results as you create them to reuse later.
memo: Dict[int, int] = {0: 0, 1: 1}  # our base cases

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # memoization
    return memo[n]


if __name__ == "__main__":
    print(fib3(40))
    print(fib3(50))
