# https://atcoder.jp/contests/abc302/tasks/abc302_b

from typing import List

H, W = [int(x) for x in input().split()]
S = [input() for _ in range(H)]


def solve(H: int, W: int, S: List[str]):
    d = (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)
    for sy in range(H):
        for sx in range(W):
            for dy, dx in d:
                if 0 <= sy + dy * 4 < H and 0 <= sx + dx * 4 < W:
                    p = [(sy + dy * i, sx + dx * i) for i in range(5)]
                    s = [S[y][x] for y, x in p]
                    if "".join(s) == "snuke":
                        for y, x in p:
                            print(y + 1, x + 1)
                        return


solve(H, W, S)
