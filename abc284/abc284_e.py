# https://atcoder.jp/contests/abc284/tasks/abc284_e

from collections import defaultdict
from sys import exit, setrecursionlimit
from typing import DefaultDict, List, Set

setrecursionlimit(300000)

N, M = [int(x) for x in input().split()]
UV = [[int(x) for x in input().split()] for _ in range(M)]


def solve(N: int, M: int, UV: List[List[int]]):
    vs: DefaultDict[int, Set[int]] = defaultdict(set)
    for u, v in UV:
        vs[u].add(v)
        vs[v].add(u)

    MRESULT = 10**6
    result = 0

    def check(st: int, ns: Set[int]):
        nonlocal result
        ns.add(st)
        result += 1
        if result >= MRESULT:
            print(MRESULT)
            exit(0)
        for d in vs[st]:
            if d not in ns:
                check(d, ns)
        ns.remove(st)

    check(1, set())

    print(result)


solve(N, M, UV)
