# https://atcoder.jp/contests/abc300/tasks/abc300_a

from typing import List

N, A, B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]


def solve(N: int, A: int, B: int, C: List[int]):
    r = A + B
    for i, x in enumerate(C):
        if x == r:
            print(i + 1)


solve(N, A, B, C)
