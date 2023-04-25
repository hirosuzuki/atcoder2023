# https://atcoder.jp/contests/abc297/tasks/abc297_c

from typing import List

H, W = [int(x) for x in input().split()]
S = [input() for _ in range(H)]


def solve(H: int, W: int, S: List[str]):
    for row in S:
        r = ""
        x = 0
        while x < W:
            if row[x : x + 2] == "TT":
                r += "PC"
                x += 2
            else:
                r += row[x]
                x += 1
        print(r)


solve(H, W, S)
