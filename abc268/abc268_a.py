# https://atcoder.jp/contests/abc268/tasks/abc268_a

from typing import List

ABCDE = [int(x) for x in input().split()]


def solve(ABCDE: List[int]):
    xs = set(ABCDE)
    result = len(xs)
    print(result)


solve(ABCDE)
