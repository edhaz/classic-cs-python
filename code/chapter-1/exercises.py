#  1. Write a different version of solving fibonnaci
import time
start_time = time.time()

def fib(n):
    memo = [0, 1]
    for _ in range(2, n + 1):
        memo.append(memo[_ - 1] + memo[_ - 2])
    return memo[n]

# print("Time taken:", time.time() - start_time)
