# https://atcoder.jp/contests/abc298/tasks/abc298_f

from collections import defaultdict
from typing import DefaultDict, List, Set, Tuple

N = int(input())
RCX = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, RCX: List[List[int]]):
    hs: DefaultDict[int, int] = defaultdict(int)
    vs: DefaultDict[int, int] = defaultdict(int)
    ps: Set[Tuple[int, int]] = set()
    for r, c, x in RCX:
        hs[r] += x
        vs[c] += x
        ps.add((r, c))

    result = 0
    for r, c, x in RCX:
        y = hs[r] + vs[c] - x
        result = max(result, y)

    hks = sorted(hs, key=lambda x: hs[x], reverse=True)
    vks = sorted(vs, key=lambda x: vs[x], reverse=True)

    for h in hks:
        for v in vks:
            if (h, v) in ps:
                continue
            y = hs[h] + vs[v]
            if y > result:
                result = y
            break

    print(result)


solve(N, RCX)
