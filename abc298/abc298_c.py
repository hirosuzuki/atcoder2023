# https://atcoder.jp/contests/abc298/tasks/abc298_c

from typing import List, Set

N = int(input())
Q = int(input())
query = [[int(x) for x in input().split()] for _ in range(Q)]


def solve(N: int, Q: int, query: List[List[int]]):
    bx: List[List[int]] = [[] for _ in range(N + 1)]
    cx: List[Set[int]] = [set() for _ in range(200000 + 1)]
    for qry in query:
        if qry[0] == 1:
            bx[qry[2]].append(qry[1])
            cx[qry[1]].add(qry[2])
        elif qry[0] == 2:
            bx[qry[1]] = sorted(bx[qry[1]])
            print(*bx[qry[1]])
        elif qry[0] == 3:
            print(*sorted(cx[qry[1]]))


solve(N, Q, query)
