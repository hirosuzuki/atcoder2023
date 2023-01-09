# https://atcoder.jp/contests/abc282/tasks/abc282_c

from typing import List

N = int(input())
S = input()


def solve(N: int, S: str):
    result: List[str] = []
    bc = 0
    for _, c in enumerate(S):
        if c == '"':
            bc += 1
        if c == "," and bc % 2 == 0:
            c = "."
        result.append(c)

    print("".join(result))


solve(N, S)
