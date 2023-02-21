# https://atcoder.jp/contests/abc290/tasks/abc290_a

from typing import List

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]


def solve(N: int, M: int, A: List[int], B: List[int]):
    result = sum(A[n - 1] for n in B)
    print(result)


solve(N, M, A, B)
