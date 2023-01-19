# https://atcoder.jp/contests/abc275/tasks/abc275_a

from typing import List

N = int(input())
H = [int(x) for x in input().split()]


def solve(N: int, H: List[int]):
    xs = [(x, i + 1) for i, x in enumerate(H)]
    xs.sort()
    print(xs[-1][1])


solve(N, H)
