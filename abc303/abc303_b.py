# https://atcoder.jp/contests/abc303/tasks/abc303_b

from typing import List, Set, Tuple

N, M = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(M)]


def solve(N: int, M: int, A: List[List[int]]):
    cs: Set[Tuple[int, int]] = set()
    for r in A:
        for x, y in zip(r, r[1:]):
            cs.add((x, y))
            cs.add((y, x))
    result = ((N * (N - 1)) - len(cs)) // 2
    print(result)


solve(N, M, A)
