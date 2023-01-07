# https://atcoder.jp/contests/abc280/tasks/abc280_a

from typing import List

H, W = [int(x) for x in input().split()]
S = [input() for _ in range(H)]

def solve(H: int, W: int, S: List[str]):
    result = 0
    for row in S:
        result += len([c for c in row if c == "#"])
    print(result)

solve(H, W, S)
