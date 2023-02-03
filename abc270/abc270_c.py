# https://atcoder.jp/contests/abc270/tasks/abc270_c

from collections import defaultdict
from sys import setrecursionlimit
from typing import DefaultDict, List, Set

setrecursionlimit(300000)

N, X, Y = [int(x) for x in input().split()]
UV = [[int(x) for x in input().split()] for _ in range(N - 1)]


def solve(N: int, X: int, Y: int, UV: List[List[int]]):
    ds: DefaultDict[int, Set[int]] = defaultdict(set)
    for u, v in UV:
        ds[u].add(v)
        ds[v].add(u)

    rs: List[int] = []
    cs: Set[int] = set()

    def calc(n: int) -> bool:
        rs.append(n)
        cs.add(n)
        if n == Y:
            print(*rs)
            return True
        for d in ds[n]:
            if d not in cs:
                if calc(d):
                    return True
        rs.pop()
        return False

    calc(X)


solve(N, X, Y, UV)
