# https://atcoder.jp/contests/abc290/tasks/abc290_d

from math import gcd
from typing import List

T = int(input())
NDK = [[int(x) for x in input().split()] for _ in range(T)]


def solve(T: int, NDK: List[List[int]]):
    for n, d, k in NDK:
        t = k - 1
        g = gcd(n, d)
        f = n * d // g
        r, ft = divmod(d * t, f)
        x = ft % n + r
        print(x)


solve(T, NDK)
