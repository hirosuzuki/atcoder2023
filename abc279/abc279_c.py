# https://atcoder.jp/contests/abc279/tasks/abc279_c

from typing import List

H, W = [int(x) for x in input().split()]
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]


def solve(H: int, W: int, S: List[str], T: List[str]):
    xs = sorted(list(zip(*S)))
    xt = sorted(list(zip(*T)))
    if xs == xt:
        print("Yes")
    else:
        print("No")


solve(H, W, S, T)
