# https://atcoder.jp/contests/abc292/tasks/abc292_d

from typing import List

N, M = [int(x) for x in input().split()]
UV = [[int(x) for x in input().split()] for _ in range(M)]


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int):
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)

    def members(self, x: int):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


def solve(N: int, M: int, UV: List[List[int]]):
    uf = UnionFind(N + 1)
    for u, v in UV:
        uf.union(u, v)

    cs: List[int] = [0] * (N + 1)
    for i in range(1, N + 1):
        cs[uf.find(i)] += 1

    vs: List[int] = [0] * (N + 1)
    for u, v in UV:
        vs[uf.find(u)] += 1
        vs[uf.find(v)] += 1

    result = all(v == c * 2 for c, v in zip(cs, vs))

    if result:
        print("Yes")
    else:
        print("No")


solve(N, M, UV)
