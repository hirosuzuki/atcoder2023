# https://atcoder.jp/contests/abc295/tasks/abc295_b

from typing import List

R, C = [int(x) for x in input().split()]
B = [input() for _ in range(R)]


def solve(R: int, C: int, B: List[str]):
    cs = [list(r) for r in B]
    for y in range(R):
        for x in range(C):
            c = B[y][x]
            if "1" <= c <= "9":
                cn = int(c)
                for dy in range(-cn, +cn + 1):
                    w = cn - abs(dy)
                    for dx in range(-w, +w + 1):
                        sx, sy = x + dx, y + dy
                        if 0 <= sx < C and 0 <= sy < R:
                            cs[sy][sx] = "."

    for r in cs:
        print(*r, sep="")


solve(R, C, B)
