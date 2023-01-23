# https://atcoder.jp/contests/abc274/tasks/abc274_b

from typing import List

H, W = [int(x) for x in input().split()]
C = [input() for _ in range(H)]


def solve(H: int, W: int, C: List[str]):
    print(*[sum(c == "#" for c in rows) for rows in zip(*C)])


solve(H, W, C)
