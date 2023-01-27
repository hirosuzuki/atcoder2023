# https://atcoder.jp/contests/abc272/tasks/abc272_a

from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    result = sum(A)
    print(result)


solve(N, A)
