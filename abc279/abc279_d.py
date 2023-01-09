# https://atcoder.jp/contests/abc279/tasks/abc279_d

from math import floor, sqrt

A, B = [int(x) for x in input().split()]


def solve(A: int, B: int):
    n = floor((A / 2 / B) ** (2 / 3) - 1)
    n = max(n, 0)

    result = min((B * i) + A / sqrt(i + 1) for i in range(n, n + 2))
    print("%.10f" % result)


solve(A, B)
