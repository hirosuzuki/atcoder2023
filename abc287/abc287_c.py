# https://atcoder.jp/contests/abc287/tasks/abc287_c

from collections import defaultdict
from typing import DefaultDict, List, Set

N, M = [int(x) for x in input().split()]
UV = [[int(x) for x in input().split()] for _ in range(M)]


def solve(N: int, M: int, UV: List[List[int]]):
    def check() -> bool:
        if N != M + 1:
            return False
        ds: DefaultDict[int, Set[int]] = defaultdict(set)
        for u, v in UV:
            ds[u].add(v)
            ds[v].add(u)

        st = -1
        for k in ds:
            if not 1 <= len(ds[k]) <= 2:
                return False
            if len(ds[k]) == 1:
                st = k

        cs: Set[int] = set()
        q: List[int] = [st]
        while q:
            x = q.pop()
            if x in cs:
                continue
            cs.add(x)
            for d in ds[x]:
                if d not in cs:
                    q.append(d)

        if len(cs) != N:
            return False

        return True

    if check():
        print("Yes")
    else:
        print("No")


solve(N, M, UV)
