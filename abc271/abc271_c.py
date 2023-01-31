# https://atcoder.jp/contests/abc271/tasks/abc271_c

from collections import deque
from typing import Deque, List, Set

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    M = 10**10
    ns: Set[int] = set(A)
    q: Deque[int] = deque(sorted(ns))
    q.extend([M] * (len(A) - len(ns)))
    result = 0
    while len(q) > 0:
        if q[0] == result + 1:
            result = q.popleft()
        elif len(q) >= 2:
            q.pop()
            q.pop()
            result += 1
        else:
            break

    print(result)


solve(N, A)
