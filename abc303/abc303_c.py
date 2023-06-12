# https://atcoder.jp/contests/abc303/tasks/abc303_c

from typing import List, Set, Tuple

N, M, H, K = [int(x) for x in input().split()]
S = input()
XY = [[int(x) for x in input().split()] for _ in range(M)]


def solve(N: int, M: int, H: int, K: int, S: str, XY: List[List[int]]):
    cs: Set[Tuple[int, int]] = set()
    for x, y in XY:
        cs.add((x, y))
    x, y, h = 0, 0, H
    for c in S:
        h -= 1
        if c == "R":
            x += 1
        elif c == "L":
            x -= 1
        elif c == "U":
            y += 1
        elif c == "D":
            y -= 1
        if h < 0:
            print("No")
            return
        if (x, y) in cs and h < K:
            h = K
            cs.remove((x, y))

    print("Yes")


solve(N, M, H, K, S, XY)
