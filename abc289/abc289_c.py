# https://atcoder.jp/contests/abc289/tasks/abc289_c

from typing import List

N, M = [int(x) for x in input().split()]
C: List[int] = []
A: List[List[int]] = []
for _ in range(M):
    C.append(int(input()))
    A.append([int(x) for x in input().split()])


def solve(N: int, M: int, C: List[int], A: List[List[int]]):
    vs: List[int] = [sum(2 ** (r - 1) for r in row) for row in A]
    result = 0
    F = 2**N - 1
    for n in range(1, 2**M):
        r = 0
        for i in range(0, M):
            if n & (2**i):
                r |= vs[i]
        if r == F:
            result += 1
    print(result)


solve(N, M, C, A)
