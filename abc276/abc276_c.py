# https://atcoder.jp/contests/abc276/tasks/abc276_c

from typing import List, Set

N = int(input())
P = [int(x) for x in input().split()]


def solve(N: int, P: List[int]):
    ns: Set[int] = set()
    nsmin = N + 1
    i = N - 1
    while i >= 0:
        if P[i] > nsmin:
            break
        else:
            nsmin = P[i]
        ns.add(P[i])
        i -= 1
    nsa = max(n for n in ns if n < P[i])
    ns.remove(nsa)
    ns.add(P[i])
    print(*P[:i], nsa, *reversed(sorted(ns)))


solve(N, P)
