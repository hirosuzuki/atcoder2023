# https://atcoder.jp/contests/abc272/tasks/abc272_c

from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    xse: List[int] = []
    xso: List[int] = []
    for x in A:
        if x % 2 == 0:
            xse.append(x)
        else:
            xso.append(x)
    xse.sort()
    xso.sort()
    rs: List[int] = []
    if len(xse) >= 2:
        rs.append(sum(xse[-2:]))
    if len(xso) >= 2:
        rs.append(sum(xso[-2:]))
    rs.sort()
    if len(rs) == 0:
        print(-1)
        return
    print(rs[-1])


solve(N, A)
