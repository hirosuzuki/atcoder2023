# https://atcoder.jp/contests/abc282/tasks/abc282_d
 
from typing import List, DefaultDict, Set, Deque, Optional, Tuple
from collections import deque, defaultdict

N, M = [int(x) for x in input().split()]
uv = [[int(x) for x in input().split()] for _ in range(M)]

def solve(N: int, M: int, uv: List[List[int]]):

    rs: DefaultDict[int, Set[int]] = defaultdict(lambda:set())
    for u, v in uv:
        rs[u].add(v) 
        rs[v].add(u) 

    cs: List[Optional[int]] = [None] * (N + 1)

    def check(st: int, v: int):
        ps = [st]
        while ps:
            nps: Set[int] = set()
            nv = v ^ 1
            for p in ps:
                cs[p] = v
                for q in rs[p]:
                    if cs[q] is None:
                        nps.add(q)
                    elif cs[q] != nv:
                        return False
            ps = nps
            v = nv
        return True

    bv = 0
    for st in range(1, N + 1):
        if cs[st] is None:
            if check(st, bv) == False:
                print(0)
                return
            bv += 2

    # print(cs, bv)

    cns = [0] * bv
    for c in cs[1:]:
        cns[c] += 1

    #print(cs, bv, cns)
    result = N * (N - 1) // 2 - M
    for b in range(bv):
        result -= cns[b] * (cns[b] - 1) // 2 
    print(result)

solve(N, M, uv)
