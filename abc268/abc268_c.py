# https://atcoder.jp/contests/abc268/tasks/abc268_c

from typing import List

N = int(input())
P = [int(x) for x in input().split()]


def solve(N: int, P: List[int]):
    rs: List[int] = [0] * N
    for i, x in enumerate(P):
        p = x - i
        rs[(p - 1) % N] += 1
        rs[(p) % N] += 1
        rs[(p + 1) % N] += 1
    result = max(rs)
    print(result)


solve(N, P)
