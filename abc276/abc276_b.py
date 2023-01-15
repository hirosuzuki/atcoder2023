# https://atcoder.jp/contests/abc276/tasks/abc276_b

from collections import defaultdict
from typing import DefaultDict, List, Set

N, M = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(M)]


def solve(N: int, M: int, AB: List[List[int]]):
    vs: DefaultDict[int, Set[int]] = defaultdict(set)
    for a, b in AB:
        vs[a].add(b)
        vs[b].add(a)
    for n in range(1, N + 1):
        print(len(vs[n]), *sorted(vs[n]))


solve(N, M, AB)
