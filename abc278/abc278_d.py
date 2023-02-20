# https://atcoder.jp/contests/abc278/tasks/abc278_d

from collections import defaultdict
from typing import DefaultDict, List, Set

N = int(input())
A = [int(x) for x in input().split()]
Q = int(input())
query = [[int(x) for x in input().split()] for _ in range(Q)]


def solve(N: int, A: List[int], Q: int, query: List[List[int]]):
    xs: DefaultDict[int, int] = defaultdict(int)
    for i, x in enumerate(A):
        xs[i + 1] = x
    for q in query:
        if q[0] == 1:
            iv = q[1]
            xs = defaultdict(lambda: iv)
        elif q[0] == 2:
            xs[q[1]] += q[2]
        elif q[0] == 3:
            print(xs[q[1]])
        # print(xs)


solve(N, A, Q, query)
