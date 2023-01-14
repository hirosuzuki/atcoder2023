# https://atcoder.jp/contests/abc277/tasks/abc277_c

from collections import defaultdict
from sys import setrecursionlimit
from typing import DefaultDict, List, Set

setrecursionlimit(210000)

N = int(input())
S = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, S: List[List[int]]):
    vs: DefaultDict[int, Set[int]] = defaultdict(set)
    for u, v in S:
        vs[u].add(v)
        vs[v].add(u)

    rn: Set[int] = set()
    maxn = 0

    def dfs(n: int):
        nonlocal maxn
        maxn = max(maxn, n)
        rn.add(n)
        for v in vs[n]:
            if v not in rn:
                dfs(v)

    dfs(1)

    print(maxn)


solve(N, S)
