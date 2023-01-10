# https://atcoder.jp/contests/abc284/tasks/abc284_a

from typing import List

N = int(input())
S = [input() for _ in range(N)]


def solve(N: int, S: List[str]):
    for r in S[::-1]:
        print(r)


solve(N, S)
