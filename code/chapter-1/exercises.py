#  1. Write a different version of solving fibonnaci
import time
start_time = time.time()

def fib(n):
    memo = [0, 1]
    for _ in range(2, n + 1):
        memo.append(memo[_ - 1] + memo[_ - 2])
    return memo[n]

# print("Time taken:", time.time() - start_time)

#  2. Create a wrapper around int that can be used as a sequence of bits
def int_decorate(func):

    def func_wrapper(name):
        return f"<p>{func(name)}</p>"

    def __getitem__(self):
        return self.

    return func_wrapper

@int_decorate
def get_int(name):
    return f"Hello {name}"


#  3. Towers of Hanoi solver

