# https://atcoder.jp/contests/abc293/tasks/abc293_b

from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    cs = [True] * N
    for i, x in enumerate(A):
        if cs[i]:
            cs[x - 1] = False
    result = [i + 1 for i, x in enumerate(cs) if x]
    print(len(result))
    print(*result)


solve(N, A)
