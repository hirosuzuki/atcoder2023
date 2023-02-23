# https://atcoder.jp/contests/abc290/tasks/abc290_c

from typing import List

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, K: int, A: List[int]):
    xs = sorted(set(A))
    result = 0
    for i in range(min(len(xs), K)):
        if xs[i] != i:
            break
        result = i + 1
    print(result)


solve(N, K, A)
