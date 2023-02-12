# https://atcoder.jp/contests/abc288/tasks/abc288_b

from typing import List

N, K = [int(x) for x in input().split()]
S = [input() for _ in range(N)]


def solve(N: int, K: int, S: List[str]):
    for x in sorted(S[:K]):
        print(x)


solve(N, K, S)
