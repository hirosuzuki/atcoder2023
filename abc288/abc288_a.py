# https://atcoder.jp/contests/abc288/tasks/abc288_a

from typing import List

N = int(input())
AB = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, AB: List[List[int]]):
    for a, b in AB:
        print(a + b)


solve(N, AB)
