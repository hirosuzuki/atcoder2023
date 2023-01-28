# https://atcoder.jp/contests/abc272/tasks/abc272_b

from collections import defaultdict
from typing import DefaultDict, List, Set

N, M = [int(x) for x in input().split()]
KX = [[int(x) for x in input().split()] for _ in range(M)]


def solve(N: int, M: int, KX: List[List[int]]):
    cs: DefaultDict[int, Set[int]] = defaultdict(set)
    for r in KX:
        for i, k1 in enumerate(r[1:-1]):
            for k2 in r[i + 2 :]:
                cs[k1].add(k2)
                cs[k2].add(k1)
    for i in range(1, N + 1):
        if len(cs[i]) != N - 1:
            print("No")
            return

    print("Yes")


solve(N, M, KX)
