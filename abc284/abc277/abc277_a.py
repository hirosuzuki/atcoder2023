# https://atcoder.jp/contests/abc277/tasks/abc277_a

from typing import List

N, X = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]


def solve(N: int, X: int, P: List[int]):
    for i, a in enumerate(P):
        if a == X:
            print(i + 1)


solve(N, X, P)
