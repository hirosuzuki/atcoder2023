# https://atcoder.jp/contests/abc274/tasks/abc274_c

from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    rs = [0] * (2 * N + 1)
    for i, x in enumerate(A):
        rs[2 * i + 1] = rs[x - 1] + 1
        rs[2 * i + 2] = rs[x - 1] + 1
    for x in rs:
        print(x)


solve(N, A)
