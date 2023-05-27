# https://atcoder.jp/contests/abc295/tasks/abc295_a

from typing import List

N = int(input())
W = [x for x in input().split()]


def solve(N: int, W: List[str]):
    if any(w in ("and", "not", "that", "the", "you") for w in W):
        print("Yes")
    else:
        print("No")


solve(N, W)
