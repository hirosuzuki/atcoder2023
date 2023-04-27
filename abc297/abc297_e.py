# https://atcoder.jp/contests/abc297/tasks/abc297_e

from heapq import heappop, heappush
from typing import List, Set

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, K: int, A: List[int]):
    cs = sorted(A)

    pushed: Set[int] = set()
    h: List[int] = []
    heappush(h, 0)
    maxx = 0
    for _ in range(K):
        e = heappop(h)
        for c in cs:
            x = e + c
            if x > maxx and len(h) > K:
                continue
            if x not in pushed:
                heappush(h, x)
                pushed.add(x)
                maxx = max(maxx, x)
        # print(e)

    result = heappop(h)
    print(result)


solve(N, K, A)
