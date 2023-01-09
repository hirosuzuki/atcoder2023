# https://atcoder.jp/contests/abc282/tasks/abc282_b

from typing import List

N, M = [int(x) for x in input().split()]
S = [input() for _ in range(N)]


def solve(N: int, M: int, S: List[str]):
    result = 0
    for i in range(N):
        for j in range(i + 1, N):
            if all(c1 == "o" or c2 == "o" for c1, c2 in zip(S[i], S[j])):
                result += 1
    print(result)


solve(N, M, S)
