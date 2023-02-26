# https://atcoder.jp/contests/abc269/tasks/abc269_b

from typing import List

S = [input() for _ in range(10)]


def solve(S: List[str]):
    ST = ["".join(r) for r in zip(*S)]
    A = min([r.index("#") for r in ST if "#" in r]) + 1
    B = max([r.rindex("#") for r in ST if "#" in r]) + 1
    C = min([r.index("#") for r in S if "#" in r]) + 1
    D = max([r.rindex("#") for r in S if "#" in r]) + 1
    print(A, B)
    print(C, D)


solve(S)
