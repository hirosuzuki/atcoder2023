# https://atcoder.jp/contests/abc300/tasks/abc300_c

from typing import List

H, W = [int(x) for x in input().split()]
C = [input() for _ in range(H)]


def solve(H: int, W: int, C: List[str]):
    cs = [list(row) + ["."] for row in C] + [["."] * (W + 1)]
    maxl = min(H, W)
    result = [0] * maxl
    for y in range(H):
        for x in range(W):
            if cs[y][x] == "#" and cs[y - 1][x - 1] == "." and cs[y + 1][x + 1] == "#":
                n = 0
                while n <= maxl:
                    if cs[y + n][x + n] != "#":
                        break
                    cs[y + n][x + n] = "*"
                    n += 1
                for i in range(n):
                    cs[y + i][x + n - 1 - i] = "*"
                result[(n - 1) // 2 - 1] += 1

    print(*result)


solve(H, W, C)
