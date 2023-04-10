# https://atcoder.jp/contests/abc297/tasks/abc297_a

from typing import List

N, D = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]


def solve(N: int, D: int, T: List[int]):
    for i in range(1, N):
        if T[i] - T[i - 1] <= D:
            print(T[i])
            return
    print(-1)


solve(N, D, T)
