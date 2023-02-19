# https://atcoder.jp/contests/abc278/tasks/abc278_c

from collections import defaultdict
from typing import DefaultDict, List, Set

N, Q = [int(x) for x in input().split()]
TAB = [[int(x) for x in input().split()] for _ in range(Q)]


def solve(N: int, Q: int, TAB: List[List[int]]):
    fs: DefaultDict[int, Set[int]] = defaultdict(set)
    for t, a, b in TAB:
        if t == 1:
            fs[a].add(b)
        elif t == 2:
            if b in fs[a]:
                fs[a].remove(b)
        elif t == 3:
            if b in fs[a] and a in fs[b]:
                print("Yes")
            else:
                print("No")


solve(N, Q, TAB)
