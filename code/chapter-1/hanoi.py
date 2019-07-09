# LIFO - Last In First Out
# eg. a stack
# pop (removes and return last item) and push (add new item)

from functools import lru_cache
from typing import TypeVar, Generic, List
T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs: int = 22
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    # print(begin, end, temp)
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a, tower_b, tower_c)
