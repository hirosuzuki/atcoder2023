# https://atcoder.jp/contests/abc295/tasks/abc295_c

from collections import Counter
from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    cs = Counter(A)
    result = sum(cs[v] // 2 for v in cs)
    print(result)


solve(N, A)
