# https://atcoder.jp/contests/abc276/tasks/abc276_d

from functools import reduce
from math import gcd
from typing import List, Tuple

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    g = reduce(gcd, A)

    def calc(n: int, m: int) -> Tuple[int, int]:
        result = 0
        d = n // m
        while d % 2 == 0:
            d //= 2
            result += 1
        while d % 3 == 0:
            d //= 3
            result += 1
        return d, result

    result = 0
    for a in A:
        n, r = calc(a, g)
        if n != 1:
            print(-1)
            return
        result += r
    print(result)


solve(N, A)
