# https://atcoder.jp/contests/abc272/tasks/abc272_d

from collections import deque
from math import floor, sqrt
from typing import Deque, Set, Tuple

N, M = [int(x) for x in input().split()]


def calc(x: int) -> Set[Tuple[int, int]]:
    result: Set[Tuple[int, int]] = set()
    n = 0
    while n * n <= x / 2:
        m = floor(sqrt(x - n * n))
        if n * n + m * m == x:
            result.add((n, m))
            result.add((-n, m))
            result.add((n, -m))
            result.add((-n, -m))
            result.add((m, n))
            result.add((-m, n))
            result.add((m, -n))
            result.add((-m, -n))
        n += 1
    return result


def solve(N: int, M: int):
    ds = calc(M)
    cs = [[-1] * N for _ in range(N)]
    q: Deque[Tuple[int, int, int]] = deque()
    q.append((0, 0, 0))
    while q:
        x, y, distance = q.popleft()
        if cs[y][x] >= 0:
            continue
        cs[y][x] = distance
        for dx, dy in ds:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N:
                if cs[ty][tx] == -1:
                    q.append((tx, ty, distance + 1))
        # print(x, y, distance)
    for r in cs:
        print(*r)


solve(N, M)
