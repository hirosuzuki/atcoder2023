# https://atcoder.jp/contests/abc274/tasks/abc274_d

from typing import List, Set

N, X, Y = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, X: int, Y: int, A: List[int]):
    def checkSingle(n: int, xs: List[int]) -> bool:
        cs: List[int] = [0] * 11
        for x in xs:
            cs[x] += 1
        ds: Set[int] = set([0])
        for i in range(1, 11):
            if cs[i] > 0:
                es = list(range(-cs[i] * i, cs[i] * i + 1, i * 2))
                ds = set([d + e for d in ds for e in es])
        return n in ds

    def check() -> bool:
        return checkSingle(X - A[0], A[2::2]) and checkSingle(Y, A[1::2])

    print(["No", "Yes"][check()])


solve(N, X, Y, A)
