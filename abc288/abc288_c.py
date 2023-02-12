# https://atcoder.jp/contests/abc288/tasks/abc288_c

from collections import defaultdict
from typing import DefaultDict, List


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

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members: DefaultDict[int, List[int]] = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


N, M = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(M)]


def solve(N: int, M: int, AB: List[List[int]]):
    uf = UnionFind(N + 1)
    r = 0
    for a, b in AB:
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
            r += 1
    print(M - r)


solve(N, M, AB)
