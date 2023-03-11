# https://atcoder.jp/contests/abc292/tasks/abc292_b

from typing import List

N, Q = [int(x) for x in input().split()]
event = [[int(x) for x in input().split()] for _ in range(Q)]


def solve(N: int, Q: int, event: List[List[int]]):
    rs: List[int] = [0] * (N + 1)
    for t, v in event:
        if t == 1:
            rs[v] += 1
        elif t == 2:
            rs[v] = 2
        elif t == 3:
            print(["No", "Yes"][rs[v] >= 2])


solve(N, Q, event)
