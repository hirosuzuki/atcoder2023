# https://atcoder.jp/contests/abc284/tasks/abc284_c

from typing import Dict, List, Set, Tuple

N, M = [int(x) for x in input().split()]
UV = [[int(x) for x in input().split()] for _ in range(M)]


def solve(N: int, M: int, UV: List[List[int]]):
    ns: Dict[int, Set[int]] = {}
    for i in range(1, N + 1):
        ns[i] = set([i])

    for u, v in UV:
        r = ns[u] | ns[v]
        for i in r:
            ns[i] = r

    cs: Set[Tuple[int, ...]] = set()
    for r in ns:
        cs.add(tuple(ns[r]))

    print(len(cs))


solve(N, M, UV)
