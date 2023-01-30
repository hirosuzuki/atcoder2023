# https://atcoder.jp/contests/abc271/tasks/abc271_b

from typing import List

N, Q = [int(x) for x in input().split()]
LA = [[int(x) for x in input().split()] for _ in range(N)]
ST = [[int(x) for x in input().split()] for _ in range(Q)]


def solve(N: int, Q: int, LA: List[List[int]], ST: List[List[int]]):
    for s, t in ST:
        print(LA[s - 1][t])


solve(N, Q, LA, ST)
