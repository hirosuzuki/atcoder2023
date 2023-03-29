# https://atcoder.jp/contests/abc295/tasks/abc295_c

from typing import List

S = input()


def solve(S: str):
    result = 0
    cs: List[int] = [0] * (2**10)
    s = 0
    cs[s] += 1
    for c in S:
        s ^= 1 << int(c)
        result += cs[s]
        cs[s] += 1
    print(result)


solve(S)
