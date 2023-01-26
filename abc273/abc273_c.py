# https://atcoder.jp/contests/abc273/tasks/abc273_c

from bisect import bisect_right
from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):

    cs = sorted(list(set(A)))

    rs: List[int] = [0] * N

    for x in A:
        r = len(cs) - bisect_right(cs, x)
        rs[r] += 1

    for x in rs:
        print(x)


solve(N, A)
