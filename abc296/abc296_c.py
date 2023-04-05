# https://atcoder.jp/contests/abc296/tasks/abc296_c

from bisect import bisect
from typing import List

N, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, X: int, A: List[int]):

    sa = set(A)

    for a in sa:
        if a + X in sa:
            print("Yes")
            return

    print("No")


solve(N, X, A)
