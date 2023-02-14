# https://atcoder.jp/contests/abc289/tasks/abc289_b

from typing import List

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, M: int, A: List[int]):
    result: List[int] = []
    rps = set(A)
    p: List[int] = []
    for x in range(1, N + 1):
        if x in rps:
            p.append(x)
        else:
            p.append(x)
            result += p[::-1]
            p.clear()
    print(*result)


solve(N, M, A)
