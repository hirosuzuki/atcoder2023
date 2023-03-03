# https://atcoder.jp/contests/abc291/tasks/abc291_b

from typing import List

N = int(input())
X = [int(x) for x in input().split()]


def solve(N: int, X: List[int]):
    result = sum(sorted(X)[N:-N]) / (N * 3)
    print(result)


solve(N, X)
