# https://atcoder.jp/contests/abc275/tasks/abc275_d

from typing import Dict

N = int(input())


def solve(N: int):

    cache: Dict[int, int] = {}

    def calc(n: int) -> int:
        if n in cache:
            return cache[n]
        if n == 0:
            return 1
        r = calc(n // 2) + calc(n // 3)
        cache[n] = r
        return r

    print(calc(N))


solve(N)
