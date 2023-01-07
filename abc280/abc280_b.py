# https://atcoder.jp/contests/abc280/tasks/abc280_b

from typing import List

N = int(input())
S = [int(x) for x in input().split()]

def solve(N: int, S: List[str]):
    result: List[int] = []
    p = 0
    for s in S:
        result.append(s - p)
        p = s
    print(*result)

solve(N, S)

