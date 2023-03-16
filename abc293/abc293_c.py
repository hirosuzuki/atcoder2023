# https://atcoder.jp/contests/abc293/tasks/abc293_c

from sys import setrecursionlimit
from typing import List, Set

setrecursionlimit(300000)

H, W = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(H)]


def solve(H: int, W: int, A: List[List[int]]):

    result = 0
    ns: Set[int] = set()

    def dfs(x: int, y: int):
        nonlocal result
        if x >= W or y >= H:
            return
        n = A[y][x]
        if n in ns:
            return
        ns.add(n)
        if x == W - 1 and y == H - 1:
            # print(ns)
            result += 1
        dfs(x + 1, y)
        dfs(x, y + 1)
        ns.remove(n)

    dfs(0, 0)
    print(result)


solve(H, W, A)
