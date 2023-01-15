# https://atcoder.jp/contests/abc277/tasks/abc277_d

from typing import Dict, List

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, M: int, A: List[int]):
    cs: Dict[int, int] = {}
    for a in A:
        if a not in cs:
            cs[a] = 0
        cs[a] += a

    ss: Dict[int, int] = {}
    for n in reversed(sorted(cs)):
        ss[n] = cs[n]
        if n + 1 in ss:
            ss[n] += ss[n + 1]

    if len(ss) == M:
        for n in ss:
            ss[n] = ss[0]
    else:
        if 0 in ss:
            for n in range(M - 1, -1, -1):
                if n not in ss:
                    break
                ss[n] += ss[0]

    result = sum(A) - max(ss.values())
    print(result)


solve(N, M, A)
