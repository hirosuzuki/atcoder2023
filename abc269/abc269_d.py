# https://atcoder.jp/contests/abc269/tasks/abc269_d

from typing import List


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


N = int(input())
XY = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, XY: List[List[int]]):
    L = 2002 * 2002
    uf = UnionFind(L)
    ps = [(x + 1000) + (y + 1000) * 2002 for x, y in XY]
    pss = set(ps)
    for p in ps:
        for d in (-2002 - 1, -2002, -1, +1, +2002, +2002 + 1):
            q = p + d
            if q in pss:
                uf.union(p, q)
    rs = set(uf.find(p) for p in ps)
    print(len(rs))


solve(N, XY)
