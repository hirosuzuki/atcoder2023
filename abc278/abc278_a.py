# https://atcoder.jp/contests/abc278/tasks/abc278_a

from typing import List

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, K: int, A: List[int]):
    xs = A[:]
    for _ in range(K):
        xs = xs[1:] + [0]
    print(*xs)


solve(N, K, A)
