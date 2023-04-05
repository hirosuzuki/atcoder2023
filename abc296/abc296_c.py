# https://atcoder.jp/contests/abc296/tasks/abc296_c

from bisect import bisect
from typing import List

N, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, X: int, A: List[int]):
    def check(t: int, xs: List[int]) -> bool:
        r = bisect(xs, t)
        if r > 0 and xs[r - 1] == t:
            return True
        return False

    xs = sorted(set(A))

    for a in xs:
        if check(a + X, xs):
            print("Yes")
            return

    print("No")


solve(N, X, A)
