# https://atcoder.jp/contests/abc291/tasks/abc291_d

from typing import List

N = int(input())
AB = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, AB: List[List[int]]):
    M = 998244353
    pa, pb = 0, 0
    na, nb = 1, 0
    for a, b in AB:
        na, nb = ((pa != a) * na + (pb != a) * nb) % M, ((pa != b) * na + (pb != b) * nb) % M
        pa, pb = a, b
    result = (na + nb) % M
    print(result)


solve(N, AB)
