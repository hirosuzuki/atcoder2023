# https://atcoder.jp/contests/abc287/tasks/abc287_b

from typing import List

N, M = [int(x) for x in input().split()]
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]


def solve(N: int, M: int, S: List[str], T: List[str]):
    xs = set(T)
    result = sum(s[-3:] in xs for s in S)
    print(result)


solve(N, M, S, T)
