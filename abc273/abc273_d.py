# https://atcoder.jp/contests/abc273/tasks/abc273_d

from bisect import bisect
from collections import defaultdict
from typing import DefaultDict, Dict, List, Set, Tuple


def fetch(s: str) -> Tuple[str, int]:
    vs = s.split()
    return vs[0], int(vs[1])


H, W, Rs, Cs = [int(x) for x in input().split()]
N = int(input())
RC = [[int(x) for x in input().split()] for _ in range(N)]
Q = int(input())
DL = [fetch(input()) for _ in range(Q)]


def solve(H: int, W: int, Rs: int, Cs: int, N: int, RC: List[List[int]], Q: int, DL: List[Tuple[str, int]]):
    yd: DefaultDict[int, Set[int]] = defaultdict(set)
    xd: DefaultDict[int, Set[int]] = defaultdict(set)
    for y, x in RC:
        yd[x].add(y)
        xd[y].add(x)

    ys: Dict[int, List[int]] = {}
    xs: Dict[int, List[int]] = {}
    for x in yd:
        ys[x] = sorted(list(yd[x]))
    for y in xd:
        xs[y] = sorted(list(xd[y]))

    # print(ys)
    # print(xs)

    y, x = Rs, Cs
    for d, l in DL:
        if d == "L":
            ps = xs[y] if y in xs else []
            p = bisect(ps, x)
            if p == 0:
                w = 1
            else:
                w = ps[p - 1] + 1
            x = max(x - l, w)
        if d == "R":
            ps = xs[y] if y in xs else []
            p = bisect(ps, x)
            if len(ps) == 0 or p >= len(ps):
                w = W
            else:
                w = ps[p] - 1
            # print("*", l, x, y, p, ps, w, H)
            x = min(x + l, w)
        if d == "U":
            ps = ys[x] if x in ys else []
            p = bisect(ps, y)
            if p == 0:
                w = 1
            else:
                w = ps[p - 1] + 1
            y = max(y - l, w)
        if d == "D":
            ps = ys[x] if x in ys else []
            p = bisect(ps, y)
            if len(ps) == 0 or p >= len(ps):
                w = H
            else:
                w = ps[p] - 1
            # print("*", l, x, y, p, ps, w, H)
            y = min(y + l, w)
        print(y, x)


solve(H, W, Rs, Cs, N, RC, Q, DL)
