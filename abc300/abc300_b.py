# https://atcoder.jp/contests/abc300/tasks/abc300_b
from typing import List

H, W = [int(x) for x in input().split()]
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]


def solve(H: int, W: int, A: List[str], B: List[str]):
    def check(i: int, j: int) -> bool:
        for y in range(H):
            for x in range(W):
                if A[(i + y) % H][(j + x) % W] != B[y][x]:
                    return False
        return True

    for i in range(H):
        for j in range(W):
            if check(i, j):
                print("Yes")
                return

    print("No")


solve(H, W, A, B)
